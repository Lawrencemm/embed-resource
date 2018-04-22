#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>


int main(int argc, char** argv)
{
  if (argc < 3)
  {
    std::cerr << "USAGE: " << argv[0] << " {sym} {rsrc}" << std::endl
              << std::endl
              << "  Creates {sym}.c from the contents of {rsrc}" << std::endl;
    return EXIT_FAILURE;
  }

  std::string sym(argv[2]);
  std::replace(sym.begin(), sym.end(), '.', '_');
  std::replace(sym.begin(), sym.end(), '-', '_');
  std::replace(sym.begin(), sym.end(), '/', '_');
  std::replace(sym.begin(), sym.end(), '\\', '_');

  std::ifstream ifs;
  ifs.open(argv[2], std::ios_base::binary);
  if (ifs.fail())
  {
    std::cout << "Failed to open " << argv[2] << '\n';
    return EXIT_FAILURE;
  }

  std::ofstream ofs;
  ofs.open(argv[1]);
  if (ofs.fail())
  {
    std::cout << "Failed to open " << argv[1] << '\n';
    return EXIT_FAILURE;
  }

  ofs << "#include <stdlib.h>" << std::endl;
  ofs << "const char _resource_" << sym << "[] = {" << std::endl;

  size_t lineCount = 0;
  char c;
  while (ifs >> c)
  {
    ofs << "0x" << std::hex << (c & 0xff) << ", ";
    if (++lineCount == 10)
    {
      ofs << std::endl;
      lineCount = 0;
    }
  }

  ofs << "};" << std::endl;
  ofs << "const size_t _resource_" << sym << "_len = sizeof(_resource_" << sym
      << ");";

  ofs.close();
  ifs.close();

  return EXIT_SUCCESS;
}
