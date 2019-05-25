__பயிற்சி__


1) இந்த நிரல் துண்டு என்ன எண்களை வெளியீடு செய்யும் ?
   `[1,2,3,4,5].each { |num| puts num if num.odd? }`

2) கீழே உள்ள 'each' என்ற ஒவ்வொன்றாக சார்பு என்ன வெளியீடு தரும் ?
   ```ruby
     "ThisdmakesdmoredsensedwithoutdD's".split("d").each {
      |letter| puts letter
    }
   ```

   குறிப்பு : இங்கு சார்புகளை கோர்வையாக இணைக்கிறோம் ('method chaining' என்று இதனை கூறுவார்கள்). முதலில் ஒரு சரம்        அணி என்பதனை உருவாக்கி பின்பு அந்த அணியில் 'ஒவ்வொன்றாக' என்ற 'each' செயல்பாடை இயக்குகிறோம். இதில் அணி          மறைமுகமாகவே உள்ளது.
   
3) 'select' என்பது தேர்ந்தெடு வாக்கியம் இந்த எண் சுருக்கு ?
   ```ruby
   food = {
     "apple" => "fruit",
     "carrot" => "vegetable",
     "tomato" => "fruit"
   }
   food.select do |item, category|
      category == "vegetable"
   end
   ```

4) கீழ் கொடுக்க பட்ட தொடர்புறு சார்பில் (map) என்ன மதிப்பு கணிக்கப்பட்டும் ?
   ```ruby
   numbers = [1,2,3,4,5]
   numbers.map { |num| num * 5 }
   ```

5) கேள்வி 4-இல் கணிக்கப்பட்ட மதிப்பு என்ன ?

