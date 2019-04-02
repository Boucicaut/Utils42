#!/usr/bin/python3

def getData(class_name : str):
    class_name_define = class_name.upper()
    bracket = '{'

    file_hpp = """#ifndef {class_define}_HPP
# define {class_define}_HPP

class {class_name}
{bracket}
public:

	{class_name}();
	~{class_name}();

private:
	{class_name}(const {class_name}&);
	{class_name} & operator=(const {class_name}&);

};

#endif
""".format(
        class_name = class_name,
        class_name_define = class_name_define,
        bracket = bracket,
    )

    file_cpp = """#include "{class_name}.hpp"

{class_name}::{class_name}()
{bracket}
}

{class_name}::~{class_name}()
{bracket}
}

{class_name}(const {class_name}& src);
{bracket}
    *this = src;
}

{class_name}& operator=(const {class_name}& src);
{bracket}
    return *this;
}""".format(
        class_name = class_name,
        bracket = bracket,
    )

    return file_hpp, file_cpp


def main(class_name : str):
    class_name = class_name.capitalize()

    file_hpp, file_cpp = getData(class_name)

    file_hpp_name = "{class_name}.hpp".format(class_name = class_name)
    with open(file_hpp_name, 'w+') as f:
        f.write(file_hpp)

    file_cpp_name = "{class_name}.cpp".format(class_name = class_name)
    with open(file_cpp_name, 'w+') as f:
        f.write(file_cpp)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 1:
        del sys.argv[0]
        for n in sys.argv:
            main(n)
    else:
        n = ""
