import argparse
import math

parser = argparse.ArgumentParser(description="Credit calculator")

parser.add_argument('--type', help='choose the type of payment')
parser.add_argument('--payment', help='annuity payment', type=int)
parser.add_argument('--principal', help='type principal', type=int)
parser.add_argument('--periods', help='type number of periods', type=int)
parser.add_argument('--interest', help='type banks interest percent', type=float)

args = parser.parse_args()
print(args)




if args.type == 'diff':
    if args.principal != None and args.periods != None and args.periods > 0 and args.interest != None:
        i = args.interest / (12 * 100)
        m = 1
        ttl = 0
        while m <= args.periods:
            d = math.ceil(args.principal / args.periods + i * (args.principal -  (args.principal * (m - 1)) / args.periods))
            print(f"Month {m}: paid out {d}")
            m += 1
            ttl += d
        ovrpmnt = ttl - args.principal
        print()
        print("Overpayment =", ovrpmnt)
    else:
        print("Incorrect parameters")

elif args.type == 'annuity':
    if args.principal != None and args.periods != None and args.interest != None and args.periods > 0:
        i = args.interest / (12 * 100)
        a_pmnt = math.ceil(args.principal * (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
        print(f"Your annuity payment = {a_pmnt}!")
        ovrpmnt = a_pmnt * args.periods - args.principal
        print("Overpayment =", ovrpmnt)

    elif args.payment != None and args.periods != None and args.interest != None and args.periods > 0:
        i = args.interest / (12 * 100)
        prcpl = math.floor(args.payment / ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)))
        print(f"Your credit principal = {prcpl}!")
        ovrpmnt = int(args.payment * args.periods - prcpl)
        print("Overpayment =", ovrpmnt)

    elif args.payment != None and args.principal != None and args.interest != None:
        i = args.interest / (12 * 100)
        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        months = n % 12
        years = n // 12

        if years == 1 and months == 1:
            print(f"You need {years} year and {months} month to repay this credit!")
        elif years == 0 and months > 1:
            print(f"You need {months} months to repay this credit!")
        elif years > 1 and months == 0:
            print(f"You need {years} years to repay this credit!")
        elif years > 1 and months > 1:
            print(f"You need {years} years and {months} months to repay this credit!")
        elif years > 1 and months == 1:
            print(f"You need {years} years and {months} month to repay this credit!")
        elif years == 1 and months > 1:
            print(f"You need {years} year and {months} months to repay this credit!")
        elif years == 1 and months == 0:
            print(f"You need {years} year to repay this credit!")
        elif years == 0 and months == 0:
            print(f"You need {years} years and {months} months to repay this credit!")
        ovrpmnt = int(args.payment * n - args.principal)
        print("Overpayment =", ovrpmnt)
    else:
        print("Incorrect parameters")

else:
    print("Incorrect parameters")
