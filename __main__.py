from jinja2 import Environment
import sys

def main():

    statment = sys.argv[1]
    arguments = sys.argv[2::]
    argv = dict()

    for a in arguments:
        name, value = a.split("=")

        print( name, value)
        argv[name] = value

    env = Environment()
    expr = env.compile_expression(statment)
    print( expr(**argv) )


main()
