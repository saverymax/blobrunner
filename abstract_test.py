from textblob import TextBlob

text = "Drosophila suzukii (Matsumura) (Diptera: Drosophilidae) is a damaging pest of fruit. Reproductively diapausing adults overwinter in woodlands and remain active on warmer winter days. It is unknown if this adult phase of the lifecycle feeds during the winter period, and what the food source may be. This study characterized the flora in the digestive tract of D. suzukii using a metagenomics approach. Live D. suzukii were trapped in four woodlands in the south of England and their guts dissected for DNA extraction and amplicon-based metagenomics sequencing (internal transcribed spacer and 16S rRNA). Analysis at genus and family taxonomic levels showed high levels of diversity with no differences in digestive tract bacterial or fungal biota between woodland sites of winter-form D. suzukii. Female D. suzukii at one site appeared to have higher bacterial diversity in the alimentary canal than males, but there was a site, sex interaction. Many of the biota were associated with cold, wet climatic conditions and decomposition. This study provides the first evidence that winter-form D. suzukii may be opportunistic feeders during the winter period and are probably exploiting food sources associated with moisture on decomposing vegetation during this time. A core gut microbiome has been identified for winter-form D. suzukii."

abstract = TextBlob(text)
print(abstract.sentiment)