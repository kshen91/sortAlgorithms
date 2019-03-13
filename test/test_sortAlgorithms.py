import pytest
import os
import importlib

modules = []
for filename in os.listdir("."):
    if filename.endswith(".py"):
        modules.append(filename[:-3])

ioPairs = [
        ([35,20,1,3,5,4,8], [1,3,4,5,8,20,35]),
        ([9,8,7,5,6,4,3,2,1],[1,2,3,4,5,6,7,8,9]),
        ([1,2,1,2,3,2,1],[1,1,1,2,2,2,3]),
        ([8554,6522,44568,0,453,8879,2313],[0,453,2313,6522,8554,8879,44568]),
        ([6,6,6,6,6],[6,6,6,6,6]),
        ([1],[1]),
        ([4493958789, 2184309723, 7471915365, 9951699844, 638745278, 3900217067, 5782162706, 1126665777, 9684445338, 4560004182, 3137107215, 9311748442, 850850650, 9280982934, 3721461635, 1452131923, 1308724051, 6073212453, 7426432734, 9727711048, 5158615380, 3059816659, 8762251215, 9278546061, 7057941618, 2960977609, 8770757330, 3152739119, 8571842562, 5743165485, 1637594646, 4947354896, 6188588081, 76549613, 2176530842, 8226343250, 982020881, 2122326113, 8217982072, 4745156912, 7363823429, 5201424252, 3231746160, 998492625, 2798915069, 1682782036, 809858350, 6938440106, 9132649312, 5832940455, 4688576632, 6202227993, 1186162710, 5157392270, 6567284795, 5044423972, 3643937544, 1637692354, 1007647596, 9736501529, 8658320423, 8213631044, 2009227144, 8606190865, 345072539, 1722165416, 7635225504, 7874825005, 4951579973, 7197506913, 5258585384, 6163891427, 6355798850, 9210934192, 8343892871, 190516650, 4086654655, 6010006448, 2290941176, 723534360, 8152412021, 7388755221, 394569090, 2732017205, 445816493, 3015156612, 6255295488, 2681556202, 1999562643, 2392030423, 1033677819, 7334005298, 9710180518, 6732749536, 545942320, 2668916547, 1534460931, 6287706592, 1385614044, 7092405077],[76549613, 190516650, 345072539, 394569090, 445816493, 545942320, 638745278, 723534360, 809858350, 850850650, 982020881, 998492625, 1007647596, 1033677819, 1126665777, 1186162710, 1308724051, 1385614044, 1452131923, 1534460931, 1637594646, 1637692354, 1682782036, 1722165416, 1999562643, 2009227144, 2122326113, 2176530842, 2184309723, 2290941176, 2392030423, 2668916547, 2681556202, 2732017205, 2798915069, 2960977609, 3015156612, 3059816659, 3137107215, 3152739119, 3231746160, 3643937544, 3721461635, 3900217067, 4086654655, 4493958789, 4560004182, 4688576632, 4745156912, 4947354896, 4951579973, 5044423972, 5157392270, 5158615380, 5201424252, 5258585384, 5743165485, 5782162706, 5832940455, 6010006448, 6073212453, 6163891427, 6188588081, 6202227993, 6255295488, 6287706592, 6355798850, 6567284795, 6732749536, 6938440106, 7057941618, 7092405077, 7197506913, 7334005298, 7363823429, 7388755221, 7426432734, 7471915365, 7635225504, 7874825005, 8152412021, 8213631044, 8217982072, 8226343250, 8343892871, 8571842562, 8606190865, 8658320423, 8762251215, 8770757330, 9132649312, 9210934192, 9278546061, 9280982934, 9311748442, 9684445338, 9710180518, 9727711048, 9736501529, 9951699844])
        ]


@pytest.mark.parametrize('modulename', modules)
@pytest.mark.parametrize('expectedIOPair', ioPairs)
def test_sortResult1(modulename, expectedIOPair):

    module = importlib.import_module(modulename)
    assert module.Runner(expectedIOPair[0]) == expectedIOPair[1]
