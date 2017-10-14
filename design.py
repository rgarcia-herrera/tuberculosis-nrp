nrp1_24 = {'path': 'data/nrp1_nrp2/norm/nrp1_24h_tb.tsv',
           'title': 'NRP1 24h'}
nrp1_48 = {'path': 'data/nrp1_nrp2/norm/nrp1_48h_tb.tsv',
           'title': 'NRP1 48h'}
nrp2_24 = {'path': 'data/nrp1_nrp2/norm/nrp2_24h_tb.tsv',
           'title': 'NRP2 24h'}
nrp2_48 = {'path': 'data/nrp1_nrp2/norm/nrp2_48h_tb.tsv',
           'title': 'NRP2 48h'}

contrasts_tb = {
    'TB NRP1 24h vs. NRP1 48h': [nrp1_24, nrp1_48],
    'TB NRP2 24h vs. NRP2 48h': [nrp2_24, nrp2_48],

    'TB NRP1 24h vs. NRP2 24h': [nrp1_24, nrp2_24],
    'TB NRP1 48h vs. NRP2 48h': [nrp1_48, nrp2_48],

# pending inter-array normalization
#    'NPR1 24h vs. LOG 24h': [],
#    'NPR1 48h vs. LOG 48h': [],

#    'LOG 24h vs. LOG 48h': [],

}
