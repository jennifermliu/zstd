Benchmarking Dictionary Builder

### Permitted Argument:
Input File/Directory (in=fileName): required; file/directory used to build dictionary; if directory, will operate recursively for files inside directory; can include multiple files/directories, each following "in="

###Running Test:
make test

###Usage:
Benchmark given input files: make ARG= followed by permitted arguments

### Examples:
make ARG="in=../../../lib/dictBuilder in=../../../lib/compress"

###Benchmarking Result:
- First Cover is optimize cover, second Cover uses optimized d and k from first one.
- For every f value of fastCover, the first one is optimize fastCover and the second one uses optimized d and k from first one.
- Fourth column is chosen d and fifth column is chosen k

github:
NODICT       0.000005       2.999642        
RANDOM       0.044155       8.791189        
LEGACY       1.121558       8.173529        
COVER       64.402024       10.652243        8          1298
COVER       6.376252       10.652243        8          1298
FAST15       9.136483       10.671076        8          1058
FAST15       0.058102       10.671076        8          1058
FAST16       8.221571       10.612941        8          1058
FAST16       0.064542       10.612941        8          1058
FAST17       9.272268       10.630593        8          1058
FAST17       0.069832       10.630593        8          1058
FAST18       9.700245       10.554097        6          1010
FAST18       0.065604       10.554097        6          1010
FAST19       9.360785       10.555720        6          1010
FAST19       0.062738       10.555720        6          1010
FAST20       8.709358       10.576349        6          1010
FAST20       0.075190       10.576349        6          1010
FAST21       10.255424       10.565525        6          1010
FAST21       0.089623       10.565525        6          1010
FAST22       10.915522       10.572912        6          1010
FAST22       0.098673       10.572912        6          1010
FAST23       11.115751       10.566912        6          1010
FAST23       0.096631       10.566912        6          1010
FAST24       11.554867       10.564108        6          1010
FAST24       0.130071       10.564108        6          1010

hg-commands:
NODICT       0.000004       2.425291        
RANDOM       0.050871       3.490331        
LEGACY       1.005231       3.911682        
COVER       67.206930       4.132653        8          386
COVER       2.951370       4.132653        8          386
FAST15       8.954460       3.929477        6          1010
FAST15       0.067525       3.929477        6          1010
FAST16       8.841976       3.989925        8          578
FAST16       0.066078       3.989925        8          578
FAST17       9.295871       4.042404        8          866
FAST17       0.080216       4.042404        8          866
FAST18       9.186789       4.064557        8          434
FAST18       0.065258       4.064557        8          434
FAST19       8.887483       4.076610        8          434
FAST19       0.076330       4.076610        8          434
FAST20       10.657517       4.072446        8          530
FAST20       0.123824       4.072446        8          530
FAST21       13.451766       4.082593        8          818
FAST21       0.151905       4.082593        8          818
FAST22       13.517087       4.063872        8          1394
FAST22       0.156180       4.063872        8          1394
FAST23       13.217273       4.081274        8          770
FAST23       0.174175       4.081274        8          770
FAST24       15.044800       4.077892        8          434
FAST24       0.186339       4.077892        8          434

hg-changelog:
NODICT       0.000004       1.377613        
RANDOM       0.262854       2.097487        
LEGACY       2.465099       2.058907        
COVER       207.047401       2.189685        8          98
COVER       7.209474       2.189685        8          98
FAST15       46.137686       2.133762        8          482
FAST15       0.332166       2.133762        8          482
FAST16       49.254704       2.142947        8          242
FAST16       0.260694       2.142947        8          242
FAST17       44.163160       2.155552        8          194
FAST17       0.264975       2.155552        8          194
FAST18       41.317318       2.169179        6          194
FAST18       0.327152       2.169179        6          194
FAST19       43.406471       2.173969        6          194
FAST19       0.289398       2.173969        6          194
FAST20       49.316699       2.178735        6          146
FAST20       0.396451       2.178735        6          146
FAST21       51.565020       2.180288        6          98
FAST21       0.411055       2.180288        6          98
FAST22       52.147931       2.179187        6          98
FAST22       0.489036       2.179187        6          98
FAST23       58.320779       2.180834        6          146
FAST23       0.528865       2.180834        6          146
FAST24       61.892978       2.180853        6          98
FAST24       0.586518       2.180853        6          98

hg-manifest:
NODICT       0.000017       1.866385        
RANDOM       0.851768       2.309436        
LEGACY       9.256718       2.506977        
COVER       995.423111       2.582528        8          434
COVER       40.695183       2.582528        8          434
FAST15       146.477445       2.407139        8          1874
FAST15       1.093513       2.407139        8          1874
FAST16       151.109093       2.485321        6          1730
FAST16       0.997846       2.485321        6          1730
FAST17       150.057535       2.532415        8          1538
FAST17       1.136178       2.532415        8          1538
FAST18       144.034948       2.559266        8          386
FAST18       0.990727       2.559266        8          386
FAST19       152.857950       2.570687        6          194
FAST19       1.117465       2.570687        6          194
FAST20       170.393246       2.572887        6          194
FAST20       1.400984       2.572887        6          194
FAST21       173.960905       2.575424        8          290
FAST21       1.962343       2.575424        8          290
FAST22       195.102604       2.578853        6          290
FAST22       1.963938       2.578853        6          290
FAST23       201.879037       2.577079        6          194
FAST23       2.466487       2.577079        6          194
FAST24       212.267988       2.579701        6          194
FAST24       2.620519       2.579701        6          194
