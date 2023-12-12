with open("input.txt", "r") as f:
    file = f.read()

allCleanedMaps = []
allRawMaps = file.split('\n\n')
seeds = list([int(x), False] for x in allRawMaps[0].replace('seeds: ', '').split(' '))
seedToSoil = allRawMaps[1].replace('seed-to-soil map:\n', '').split('\n')
allCleanedMaps.append(seedToSoil)
soilToFertilizer = allRawMaps[2].replace('soil-to-fertilizer map:\n', '').split('\n')
allCleanedMaps.append(soilToFertilizer)
fertilizerToWater = allRawMaps[3].replace('fertilizer-to-water map:\n', '').split('\n')
allCleanedMaps.append(fertilizerToWater)
waterToLight = allRawMaps[4].replace('water-to-light map:\n', '').split('\n')
allCleanedMaps.append(waterToLight)
lightToTemp = allRawMaps[5].replace('light-to-temperature map:\n', '').split('\n')
allCleanedMaps.append(lightToTemp)
tempToHumidity = allRawMaps[6].replace('temperature-to-humidity map:\n', '').split('\n')
allCleanedMaps.append(tempToHumidity)
humidityToLocation = allRawMaps[7].replace('humidity-to-location map:\n', '').split('\n')
allCleanedMaps.append(humidityToLocation)

for mappings in allCleanedMaps:
    for mapping in mappings:
        mapSetList = [int(x) for x in mapping.split(' ')]
        destRange = mapSetList[0]
        srcRange = mapSetList[1]
        rangeLength = mapSetList[2]
        for idx,seed in enumerate(seeds):
            if seed[0] in range(srcRange,srcRange+rangeLength) and seed[1] is False:
                seeds[idx][0] = seed[0] + destRange - srcRange
                seeds[idx][1] = True
    for seed in seeds:
        seed[1] = False
            
minSeed = min(seeds)
print(minSeed[0])