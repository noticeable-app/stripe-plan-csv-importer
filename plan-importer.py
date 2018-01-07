#!/bin/python

import csv
import stripe
import sys

stripe.api_key = sys.argv[1]

firstline = True

with open(sys.argv[2], 'rb') as csvfile:
    plans = csv.reader(csvfile, delimiter=',')
    for plan in plans:
        if firstline:
            firstline = False
            continue

        try:
            stripe.Plan.create(
                amount=int(plan[4]),
                interval=plan[3],
                name=plan[1],
                currency=plan[5],
                id=plan[0],
                trial_period_days=0 if plan[7] == '' else int(plan[7])
            )
            print plan[0] + ' created!'
        except Exception as e:
            print plan[0] + ' -> '+ str(e)
