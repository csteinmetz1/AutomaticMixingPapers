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

    approaches_by_year = {'GT' : years.copy(),
                          'KE' : years.copy(),
                          'ML' : years.copy()}

    categories_by_year = {'Level' : years.copy(), 
                          'Panning' : years.copy(),
                          'Equalization' : years.copy(),
                          'Compression' : years.copy(),
                          'Reverb' : years.copy(),
                          'Integrated' : years.copy()}
   
    with open(filename, "r+") as mixing:
        mixing_tsv = csv.DictReader(mixing, dialect='excel-tab')
        f = mixing_tsv.fieldnames

        for entry in mixing_tsv:
            # get attributes from table
            year      = entry['Year']
            category  = entry['Category']
            approach  = entry['Approach']

            years[year]          += 1
            categories[category] += 1
            approaches[approach] += 1
            
            categories_by_year[category][year] += 1
            approaches_by_year[approach][year] += 1

            total_pubs += 1

    # set up plot colors
    level_color = '#151c53'
    pan_color = '#1f347e'
    eq_color = '#2b609d'
    comp_color = '#3993bd'
    verb_color = '#65bbca'
    int_color = '#b6dbc5'

    GT_color = '#461a68'
    KE_color = '#9d3484'
    ML_color = '#ec7a8a'  

    # plot publications by year
    years_num = [int(i) for i in sorted(years.keys())]
    pubs_per_year = [i[1] for i in sorted(years.items())]
    plt.figure(0)
    plt.bar(years_num, pubs_per_year, align='center', color='#A9E8DC')
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(years_num, years_num, rotation='vertical')
    plt.ylabel('Publications')
    plt.title('Automatic Mixing Publications by Year')
    plt.savefig('figs/papers_by_year.png', bbox_inches="tight", transparent=True)

    # plot publications by year with division by approach
    years_num = [int(i) for i in sorted(years.keys())]
    GT_pubs_by_year = np.array([i[1] for i in sorted(approaches_by_year['GT'].items())])
    KE_pubs_by_year = np.array([i[1] for i in sorted(approaches_by_year['KE'].items())])
    ML_pubs_by_year = np.array([i[1] for i in sorted(approaches_by_year['ML'].items())])
    plt.figure(1)
    p1 = plt.bar(years_num, GT_pubs_by_year, align='center', color=GT_color)
    p2 = plt.bar(years_num, KE_pubs_by_year, bottom=GT_pubs_by_year, align='center', color=KE_color)
    p3 = plt.bar(years_num, ML_pubs_by_year, bottom=GT_pubs_by_year+KE_pubs_by_year, align='center', color=ML_color)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(years_num, years_num, rotation='vertical')
    plt.ylabel('Publications')
    plt.title('Automatic Mixing Publications by Year: Approach Breakdown', y=1.08)
    lgd = plt.legend((p3[0], p2[0], p1[0]), ('Machine Learning', 'Knowledge Engineering', 'Grounded Theory'), loc=3, bbox_to_anchor=(1, 0.5))
    plt.savefig('figs/approaches_by_year.png', additional_artists=lgd, bbox_inches="tight", transparent=True)

    # plot publications by year with division by category
    years_num = [int(i) for i in sorted(years.keys())]
    level_pubs_by_year = np.array([i[1] for i in sorted(categories_by_year['Level'].items())])
    pan_pubs_by_year = np.array([i[1] for i in sorted(categories_by_year['Panning'].items())])
    eq_pubs_by_year = np.array([i[1] for i in sorted(categories_by_year['Equalization'].items())])
    comp_pubs_by_year = np.array([i[1] for i in sorted(categories_by_year['Compression'].items())])
    verb_pubs_by_year = np.array([i[1] for i in sorted(categories_by_year['Reverb'].items())])
    int_pubs_by_year = np.array([i[1] for i in sorted(categories_by_year['Integrated'].items())])
    plt.figure(2)
    p1 = plt.bar(years_num, level_pubs_by_year, align='center', color=level_color)
    p2 = plt.bar(years_num, pan_pubs_by_year, bottom=level_pubs_by_year, align='center', color=pan_color)
    p3 = plt.bar(years_num, eq_pubs_by_year, bottom=level_pubs_by_year+pan_pubs_by_year, align='center', color=eq_color)
    p4 = plt.bar(years_num, comp_pubs_by_year, bottom=level_pubs_by_year+pan_pubs_by_year+eq_pubs_by_year, align='center', color=comp_color)
    p5 = plt.bar(years_num, verb_pubs_by_year, bottom=level_pubs_by_year+pan_pubs_by_year+eq_pubs_by_year+comp_pubs_by_year, align='center', color=verb_color)
    p6 = plt.bar(years_num, int_pubs_by_year, bottom=level_pubs_by_year+pan_pubs_by_year+eq_pubs_by_year+comp_pubs_by_year+verb_pubs_by_year, align='center', color=int_color)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.xticks(years_num, years_num, rotation='vertical')
    plt.ylabel('Publications')
    plt.title('Automatic Mixing Publications by Year: Category Breakdown', y=1.08)
    lgd = plt.legend((p6[0], p5[0], p4[0], p3[0], p2[0], p1[0]), ('Level', 'Panning', 'Equalization', 'Compression', 'Reverb', 'Integrated'), loc=3, bbox_to_anchor=(1, 0.5))
    plt.savefig('figs/categories_by_year.png',  additional_artists=lgd, bbox_inches="tight",  transparent=True)

    # plot pie chart of approaches
    plt.figure(3)
    labels = ['Grounded Theory', 'Knowledge Engineering', 'Machine Learning']
    sizes = approaches.values()
    colors = [GT_color, KE_color, ML_color]
    ax = plt.subplot(111)
    details = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    for wedge in details[0]:
        wedge.set_edgecolor('white')
    for perct in details[2]:
        perct.set_color('white')
    ax.axis('equal')
    plt.savefig('figs/approaches_breakdown.png', transparent=True)

    # plot pie chart of categories
    plt.figure(4)
    labels = categories.keys()
    sizes = categories.values()
    colors = [level_color, pan_color, eq_color, comp_color, verb_color, int_color]
    ax = plt.subplot(111)
    details = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    for wedge in details[0]:
        wedge.set_edgecolor('white')
    for perct in details[2]:
        perct.set_color('white')
    plt.axis('equal')
    plt.savefig('figs/categories_breakdown.png',  transparent=True)

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

    with open("README.md", "w+") as readme_file, open('header.md') as header, open('acknowledgments.md') as ack, open('contribute.md') as contrib:
        readme_file.write(header.read())

        for section in sections:
            readme_file.write(sections[section])
        
        stats = """# Statistics\n"""
        stats += """![pubs_by_year](figs/papers_by_year.png)\n"""
        stats += """![categories_by_year](figs/categories_by_year.png)\n"""
        stats += """![approaches_by_year](figs/approaches_by_year.png)\n"""
        stats += """![categories](figs/categories_breakdown.png)\n"""
        stats += """![approaches](figs/approaches_breakdown.png)\n"""
        readme_file.write(stats)
        readme_file.write(ack.read())
        readme_file.write(contrib.read())
        
    num_papers = mixing.line_num - 1
    return num_papers

def main(filename="mixingpapers.tsv"):
    sort_papers_by_year(filename)
    calculate_statistics(filename)
    num_papers = build_readme(filename)
    print("Compiled " + str(num_papers) + " papers")

if __name__ == "__main__":
    main("mixingpapers.tsv")