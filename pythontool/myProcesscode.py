from ImageProcess import Graphics


g = Graphics('waiting/1.jpg','finished/1.jpg');
print(g.infile);
print(g.outfile);
g.resize_by_size(200);


