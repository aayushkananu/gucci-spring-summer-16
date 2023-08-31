#### COLLECTION ####
gucci_collection_name = " GUCCI SS16"

## DEFINE THE TRENDS
gucci_trends = {
  'logo_belt': 0
}  

## DEFINE THE LOOKS
gucci_looks = [
  [], 
  [], 
  [], 
  [], 
  [1],
  [], 
  [], 
  
['black','close_toed','goggles','blazer'],
['black','polka_dots','stockings' ,'ankle_strap'],
['pink','black','white','googles','cape','fishnet','polka_dots','stockings','platform_heels'],
['black','pink','parachute_pant','long_coat'],
['pink','silk','maxi'],
['long_coat','brown','white','pink', 'bow', 'fur','ballet_flats'],
['brown','ruffle','ballet_flats'],
['brown','shimmer','gloves','ballet_flats'],
['shimmer','blue','black','button_up','long_coat','boots'],
['orange','purple','bow','gloves','platform_heels'],
['ruffle','long_coat','plaform_heels' ,'leggings','orange'],
['pink','brown','parachute_pants'],
['ruffle','shimmer','red','pink','ballet_flats'],
['leggings','green','shimmer','pink','ruffle','gloves','ballet_flats'],
['ruffle','pink','black','brown','gloves','ballet_flats'],
['long_coat','leggings','platform_heels','ruffle','brown','green','pink'],
['long_coat', 'ruffle','polka_dots' 'stockings','green','ballet_flats','black','white'], #look18
['ruffle','cape', 'stripes','ballet_flats','pink','black','green'],
['pink', 'long_coat','white','black',],
['pink','maxi','bow', 'close_toed'],
['pink','black', 'gloves', 'maxi', 'polka_dots','ruffle','close_toed'],
['ruffle','gloves','ballet_flats' ,'pink','black','green'],
['stripes','pink','bow','black','yellow', 'ballet_flats'],
['cape','pink','shimmer','fur', 'bow', 'ballet_flats'],
['black', 'gloves', 'ballet_flats'],
['cape','black','ankle_strap'] , #look27
['tie','boots','button_up','black','white'],
['fishnet','ruffle','black'],
['black','feather','ankle_strap','pink'],
['black','maxi','bow','white'],
['long coat','fur','button_up','blue'],
['blazer','tie','button_up','shimmer','black','white'],
['striped','blazer','bow','pink', 'ballet_skirt','black','white'],
['blazer','ruffle','shimmer','fishnet','stockings','gloves','black','white'],
['black','gloves'],
['white','net','ballet_flats'],
['white','maxi','black','bow'],
['polka_dots', 'white','maxi','close_toed','ankle_strap','brown'],
['blazer','boots','tie','button_up','yellow','black','white'],
['tie','button_up','yellow', 'white','black','polka_dots'],
['polka dots','long_coat','bow','tie','button_up','ballet_flats','black,'blue','off_white'],
['bow','green', 'maxi','platform_heels'],
['ruffle','maxi','platform_heels','green','black'], #look44
['purple','sheer','maxi_dress', 'bow'], # LOOK 45
['purple', 'black', 'stockings', 'gloves', 'leather', 'purple' 'ballet_flats','bow'],
['platform_heels', 'purple', 'maxi_dress', 'asymmetric'],
['blazer', 'tie', 'button_down', 'purple', 'boots', 'leather'],
['purple', 'ruffles','maxi_dress', 'white', 'bow'],
['yellow', 'purple', 'black','bow', 'blazer'],
['ruffles', 'yellow', 'pink','ankle_straps'],
['bow', 'gloves','purple', 'pink', 'red', 'maxi_dress'],
['ruffles', 'purple', 'red', 'stiletto', 'gloves', 'leather'],
['red', 'pink', 'leahter', 'blazer'],
['red', 'leather', 'gloves'], #LOOK  55
['blazer', 'red', 'shimmer'],
['red','floral', 'stiletto'],
['tie', 'red', 'leather', 'feathers'],
['red', 'platform_heels','sheer'],
['bow', 'red', 'maxi_dress'],
['ruffles','sheer', 'shimmer','silver'],
['pink','silver','shimmer'],
['gold','ruffles','shimmer'],
['pink','blazer', 'leather'],
['leather', 'gloves','shimmer','green'],
['blazer','green','leather'],
['blue','maxi_dress','platform_heels'],
['silver','bow','shimmer','sheer'],
['pink','stocking','shimmer','bow'],
['ruffles','silver','platform_heels'],
['stocking','shimmer','gloves','leather'],
['yellow','silver','ruffles'],
['golden', 'pink','maxi_dress','shimmer'],
['pink','shimmer','leather'],
['mini_skirt', 'shimmer','stocking','leather','sheer'],
['leather','platform_shoes','sheer'],
['bow'],
['blazer','leather','sheer'],
['ruffles','stocking','sheer','mini_skirt'],
['pink','feather','polka_dots','stocking'],
['bow','pink','gloves','platform_heels'],
['tie','leather','shimmer'],
['pink','mini_skirt','shimmer','platform_heels'],
['pink','leather','gloves'],
['ruffles','shimmer','pink','leather'],
['shimmer','ruffles'],
['ruffles'],
['ruffles'],
['ruffles','feather','polka_dots','shimmer','bow']
]

collection_name = valentino_collection_name
looks = valentino_looks
total = len(looks)
trends = valentino_trends

## PRINT INFO:
print("ANALYZING TRENDS FROM", collection_name)

## TREND DATA (count)
for trend, var in trends.items():
    count = 0
    for look in looks:
        if str(trend) in look:
            count += 1
    trends.update({trend:count})

## GET PERCENTAGES

trend_percentages = {}
for trend, var in trends.items():
    percentage = var / total * 100
    trend_percentages.update({trend: percentage})
    print("PERCENTAGE OF %s : %s" % (trend, percentage))




















