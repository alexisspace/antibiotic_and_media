# antibiotic_and_media
For the calculations involved in the preparation of antibiotic selective media. This includes stock concentrations, media mass and volume and dilution calculations of antibiotic in media

The script has three parts

## PART I 
Is for the calculation of the required volume of water to be added to a specified mass of antibiotic.
The relevant variables are:

`stock_concentration` (mg/mL): This the standard recommended stock concentration given by the manufacturer. See https://www.addgene.org/mol-bio-reference/#antibiotics for a list of standard stock concentrations in several antibiotics.

`antibiotic_mass` (mg): This is the mass you want to use for the mix in stock concentration. The advantage is that you don’t need to use all the powder antibiotic you have at once, given the fact that some antibiotics are more stable in powder form.

***The result of this part is the amount of water you have to add to the given mass of antibiotic you want to save in stock concentration***

## PART II 
Is for media calculations, relevant variables are:
`lb_agar_concentration` (mg/mL): this is provided by the media manufacturer, the amount of mass per milliliter of water. See http://www.the-odin.com/lb-agar/ for an example
`v_plate` (mL): The volume of the plates you are working with.

`n_plates` (number of plates desired to fill): The number of plates you want to fill with media.

`v_plates_total` (mL): This is where the total volume of media is calculated (number of plates multiplied by the volume of each plate) YOU CAN IGNORE v_plate AND n_plates AND HARDCODE THE VALUE of v_plates_total = SOME_VALUE if you are using liquid media

***The result of this part is the necessary mass of media to be added to the total volume of media (calculated or hardcoded)***

## PART II 
Is for the calculation of the required volume of antibiotic in stock concentration form to be present in the total volume of media required, relevant variables are:

`c1` (mg/mL): Antibiotic stock concentration, this value is set to value given in PART I but you can change it if you want to use this part of the code independently for the other ones.

`c2` (mg/mL): is the final desired concentration (working concentration). See https://www.addgene.org/mol-bio-reference/#antibiotics for a list of standard working concentrations in several antibiotics.

`v2` (mL): is the final desired volume of media, this is set to the previous calculated value in PART II but again you can change it here if you want.

***The result of this part is the necessary volume of antibiotic in the stock concentration form to be present the final volume of media***

