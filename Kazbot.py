#!/usr/bin/env python3

import sys
import argparse

def get_args(argv):
    parser = argparse.ArgumentParser(
        prog = 'KazBot',
        description = 'Hopefully an autotrader for crypto currencies'
    )

    parser.add_argument("-c", "--config", required=True, type=argparse.FileType('r'))

    args = parser.parse_args(argv)

    # TODO: Open config to list

    parser.add_argument("-a", "--action", choices=["test", "simulate", "run"], default="simulate")
    parser.add_argument("-s", "--strategy", help="Strategy to utilize for auto trading. Options:", choices=['StochRSI', 'EMA', 'MACD'], default = "StochRSI")
    parser.add_argument("-t", "--cycle_time", help="Number of minutes in trading cycles", type=int)

    # TODO: Parse the JSON first, and then the argv second (argv)
    # TODO: Based on action and strategy, add other arguments using parent

    # Simulation Parser
    sim_parser = argparse.ArgumentParser()
    sim_parser.add_argument("--start_val", help="for simulations, USD to begin with")
    sim_parser.add_argument("--start_date", help="for simulations, date to start simulation (YYYY-MM-DD)")
    sim_parser.add_argument("--end_date", help="for simluations, date to end simulation")
    
    

    return(args)


if __name__ == "__main__":
    args = get_args(sys.argv[1:])