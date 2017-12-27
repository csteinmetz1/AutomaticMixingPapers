import csv
import operator
import matplotlib.pyplot as plt
import numpy as np

def calculate_statistics(filename):
    years = {'2007' : 0, '2008' : 0, '2009' : 0, '2010' : 0,
             '2011' : 0, '2012' : 0, '2013' : 0, '2014' : 0,
             '2015' : 0, '2016' : 0, '2017' : 0, '2018' : 0}
    
    categories = {'Level' : 0, 
                  'Panning' : 0,
                  'Equalization' : 0,
                  'Compression' : 0,
                  'Reverb' : 0,
                  'Integrated' : 0}
    
    approaches = {'GT' : 0, 'KE' : 0, 'ML' : 0}

    total_pubs = 0
    
    with open(filename, "r+") as mixing:
        mixing_tsv = csv.DictReader(mixing, dialect='excel-tab')
        f = mixing_tsv.fieldnames

        for entry in mixing_tsv:
            # get attributes from table
            year      = entry['Year']
            category  = entry['Category']
            approach  = entry['Approach']

            years[year] += 1
            categories[category] += 1
            approaches[approach] += 1
            total_pubs += 1

    # plot publications by year
    years_num = [int(i) for i in sorted(years.keys())]
    pubs_per_year = [i[1] for i in sorted(years.items())]
    plt.figure(0)
    plt.bar(years_num, pubs_per_year, align='center')
    plt.xticks(years_num, years_num, rotation='vertical')
    plt.xlabel('Year')
    plt.ylabel('Publications')
    plt.title('Automatic Mixing Publications by Year')
    plt.savefig('figs/papers_by_year.png')

    # plot pie chart of approaches
    plt.figure(1)
    labels = approaches.keys()
    sizes = approaches.values()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.savefig('figs/approaches_breakdown.png')

    # plot pie chart of categories
    plt.figure(2)
    labels = categories.keys()
    sizes = categories.values()
    #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.savefig('figs/categories_breakdown.png')

def sort_papers_by_year(filename):
    with open(filename, "r+") as mixing:
        mixing_tsv = csv.DictReader(mixing, dialect='excel-tab')
        f = mixing_tsv.fieldnames

        sorted_mixing = sorted(mixing_tsv, key=operator.itemgetter('Year'), reverse=True)
        
        mixing.seek(0)
        writer = csv.DictWriter(mixing, delimiter='\t', dialect='excel-tab', fieldnames=f)
        writer.writeheader()
        for row in sorted_mixing:
            writer.writerow(row)
        mixing.truncate()

def build_readme(filename):
    # define dict of section holders
    sections = {'Level' : "", 
                'Panning' : "",
                'Equalization' : "",
                'Compression' : "",
                'Reverb' : "",
                'Integrated' : ""}

    with open(filename) as mixing:
        mixing = csv.DictReader(mixing, dialect='excel-tab')
        
        # get column labels
        f = mixing.fieldnames
        
        # initalize table for each section
        for section in sections:
            sections[section] = "## " + section + "\n|%s|%s|%s|%s|%s|\n" %(f[0], f[1], f[2], f[6], f[4]) + "|---|---|---|---|---|\n"

        for entry in mixing:
            # get attributes from table
            year      = entry['Year']
            title     = entry['Title']
            authors   = entry['Authors']
            paper     = entry['Paper']
            resources = entry['Resources']
            category  = entry['Category']
            approach  = entry['Approach']
            
            if resources == "No":
                sections[category] += "|%s|[%s](%s)|%s|%s|%s|\n" %(year, title, paper, authors, approach, resources)
            else:
                sections[category] += "|%s|[%s](%s)|%s|%s|[Yes](%s)|\n" %(year, title, paper, authors, approach, resources)

    with open("README.md", "w+") as readme_file, open('header.md') as header:
        readme_file.write(header.read())

        for section in sections:
            readme_file.write(sections[section])
        
        stats = """# Statistics\n"""
        stats += """![pubs_by_year](figs/papers_by_year.png)\n"""
        stats += """![categories](figs/categories_breakdown.png)\n"""
        stats += """![approaches](figs/approaches_breakdown.png)\n"""
        readme_file.write(stats)
        
    num_papers = mixing.line_num - 1
    return num_papers

def main(filename="mixingpapers.tsv"):
    sort_papers_by_year(filename)
    calculate_statistics(filename)
    num_papers = build_readme(filename)
    print("Compiled " + str(num_papers) + " papers")

if __name__ == "__main__":
    main("mixingpapers.tsv")