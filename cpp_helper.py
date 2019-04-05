#!/usr/bin/python3

import argparse

def getData(class_name : str):
    class_name_define = class_name.upper()
    obracket = '{'
    cbracket = '}'

    file_hpp = """#ifndef {class_define}_HPP
# define {class_define}_HPP

class {class_name}
{obracket}
public:

	{class_name}();
	~{class_name}();

private:
	{class_name}(const {class_name}&);
	{class_name} & operator=(const {class_name}&);

{cbracket};

#endif
""".format(
        class_name = class_name,
        class_define = class_name_define,
        obracket = obracket,
        cbracket = cbracket,
    )

    file_cpp = """#include "{class_name}.hpp"

/*
** Builtin functions
*/

{class_name}::{class_name}()
{obracket}
{cbracket}

{class_name}::~{class_name}()
{obracket}
{cbracket}

{class_name}(const {class_name}& src);
{obracket}
    *this = src;
{cbracket}

{class_name}& operator=(const {class_name}& src);
{obracket}
    return *this;
{cbracket}

/*
** Class Specific functions
*/

""".format(
        class_name = class_name,
        obracket = obracket,
        cbracket = cbracket,
    )

    return file_hpp, file_cpp


def main(class_name : str):
    # class_name = class_name.capitalize()

    file_hpp, file_cpp = getData(class_name)

    file_hpp_name = "{class_name}.hpp".format(class_name = class_name)
    with open(file_hpp_name, 'w+') as f:
        f.write(file_hpp)

    file_cpp_name = "{class_name}.cpp".format(class_name = class_name)
    with open(file_cpp_name, 'w+') as f:
        f.write(file_cpp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c", "--classes", nargs='+', type=str,
        help="Class names to implements", default=None, required=True,
    )

    args = parser.parse_args()

    for class_name in args.classes:
        main(class_name)

    exit(0)
