#include <iostream>

#include "Resource.h"

LOAD_RESOURCE(text_resource, resource_txt);

int main() {
    std::cout << text_resource.toString() << std::endl;
}
