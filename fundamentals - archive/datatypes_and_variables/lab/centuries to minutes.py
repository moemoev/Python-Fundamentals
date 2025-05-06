quantity_by_timescale = {'centuries': int(input())}
quantity_by_timescale.update({'years': quantity_by_timescale['centuries'] * 100})
quantity_by_timescale.update({'days': int(quantity_by_timescale['years'] * 365.2422)})
quantity_by_timescale.update({'hours': quantity_by_timescale['days'] * 24})
quantity_by_timescale.update({'minutes': quantity_by_timescale['hours'] * 60})

values = []

for key, value in quantity_by_timescale.items():
    values.append(str(value) + " " + key)
print(" = ".join(values))
