#!/usr/bin/python
# Start
# Multiprocessing for running different parts of programm and 
# probably sharing data between of them
# Modules
import argparse
import multiprocessing
import os
import sys


def handle_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--concurrency", type=int,
                        default=multiprocessing.cpu_count(),
                        help="""(specifing the concurrency
                            for debugging and timing) [default: (default)d""")
    parser.add_argument("-s", "--size", default=400, type=int,
                        help="""make a scaled image that fits
                        the given dimension [default: %(default)d]""")
    
    parser.add_argument("-S", "--smooth", action="store_true",
                        help="use smooth scaling (slow but good for text)")
    
    parser.add_argument("source", help="""the directory containing the original
                         .xpm images""")

    parser.add_argument("target", help="the directory for the scaled .xpm images")
    
    args = parser.parse_args()
    source = os.path.abspath(args.source)
    target = os.path.abspath(args.source)
    if source == target:
        args.error("source and target most be different")
    if not os.path.exists(target):
        os.makedirs(target)
    return args.size, args.smooth, source, target, args.concurrency










# End