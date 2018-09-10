import sys

def get_stats(types):
    count = 1
    total = 0
    for key,val in types.iteritems():
        total += val
        print "%d-%s: %d" % (count, key, val)
        count += 1
        
    print "_" * 80
    print "Total: %s\n\n" % (total)

gene_types = {}
transcript_types = {}
    
#with open("gencode.v28.primary_assembly.annotation.gtf","r") as gtf:

for line in sys.stdin:

    if "#" in line:
        continue

    fields = line.strip().split("\t")
    feature_type = fields[2]
    info = fields[-1].split("; ")

    if feature_type == "gene":
        gene_type = info[1].replace('"','').split()[1]
        if gene_type in gene_types:
            gene_types[gene_type] += 1
        else:
            gene_types[gene_type] = 1
    
    elif feature_type == "transcript":
        transcript_type = info[4].replace('"','').split()[1]
        if transcript_type in transcript_types:
            transcript_types[transcript_type] += 1
        else:
            transcript_types[transcript_type] = 1
        
    else:
        continue


print "Genes Stats:\n"
get_stats(gene_types)
print "Transcripts Stats: \n"
get_stats(transcript_types)