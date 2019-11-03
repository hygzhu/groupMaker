import sys
import csv
import itertools
from operator import itemgetter


def main():
        print("File name: " + sys.argv[1])

        rankings = dict()
        people = list()
        group_rankings = dict()
        final_group_list = list()

        #Read rankings from CSV
        with open(sys.argv[1], newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in list(reader)[1:]:
                #Extract and clean row
                row = row[3][7:].split("\"")
                row = [ x for x in row if x.isdigit() ]

                #Add to data
                people.append(int(row[0]))
                for idx, value in enumerate(row[1:]):
                    rankings[(int(row[0]), idx + 1)] = int(value)

        #Generate all combinations of groups and assign values
        combinations = list(itertools.combinations(people, 2))

        for group in combinations:
            group_value = 0
            possible_links = list(itertools.combinations(list(group), 2))
            #Sum up all possible rankings
            for link in possible_links:
                group_value += rankings[link]
                group_value += rankings[(link[1], link[0])]

                group_rankings[group] = group_value

        #Sort values of dict
        sorted_groups = sorted(group_rankings.items(), key=lambda x: x[1], reverse=True)
        while len(sorted_groups) > 0:
            best_group = sorted_groups.pop(0)
            final_group_list.append(best_group[0])

            sorted_groups = list(filter(lambda group: not any(x in list(best_group[0]) for x in list(group[0])), sorted_groups))

        print(final_group_list)

if __name__ == "__main__":
    main()