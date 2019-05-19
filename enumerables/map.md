
##Map

Last but not least, let’s check out the map method. So far we’ve seen how different methods affect elements from our collections. With map, we can select certain elements and modify them at the same time. Let’s jump into an example.

```ruby
["dog", "cat", "snake", "mouse"].map do |animal|
  animal.capitalize
end
=> ["Dog", "Cat", "Snake", "Mouse"]
```

Here we have an array of animals. We decide we want to capitalize each animal name. So we call map on the array and another built in Ruby method, `capitalize`, on each item in the array. The capitalize method takes a string and makes its first letter capitalized.

Cool, right? Map essentially finds and manipulates the data in the array, or maps your block of code to each specific element in that array. To permanently alter an array with the map feature in Ruby, simply add the exclamation point to modify the existing array.

```ruby
animals = ["dog","cat","snake","mouse"]
animals.map! { |animal| animal.capitalize }
=> ["Dog", "Cat", "Snake", "Mouse"]

animals
=> ["Dog", "Cat", "Snake", "Mouse"]
```

At this point you understand two fundamental collections in programming languages: arrays and hashes. After diving into the Enumerable module we revealed four of the most common methods used on these collections; each, each\_with\_index, select and map. Now it’s time to test your knowledge with a few more examples.

<div style="height:30px;"></div>

## தொர்புரு அணி (map) 

அறுதியும் இறுதியுமாக தொர்புரு அணி(map) முறையை பாருங்கள். நம் சேகரிப்புகளிலுள்ள கூறுகளை(elements) வேறுபட்ட முறைகள் எவ்வாறு பாதிக்கின்றன என்பதை இதுவரை பார்த்தோம்.தொர்புரு அணி முறை மூலம் குறிப்பிட்ட கூறுகளை தேர்ந்தெடுத்து ஒரே நேரத்தில் திருத்தலாம். உதாரணமாக

["dog", "cat", "snake", "mouse"].map do |animal|
  animal.capitalize
end
=> ["Dog", "Cat", "Snake", "Mouse"]

இங்கே நாம் ஒரு விலங்குகளின் அணியை  வைத்திருக்கிறோம். அணியிலுள்ள ஒவ்வொரு விலங்குகளின் முதல் எழுத்தையும் ஆங்கில பெரிய எழுத்துக்களால் மாற்றீடு செய்ய ரூபியிலுள்ள தொர்புரு அணி(map) முறைமையை பயன்படுத்துவதோடு capitalize முறையையும் பயன்படுத்துகின்றோம் .capitalize முறைமை அணியிலுள்ள விலங்குகள் எல்லாவற்றினதும் முதல் எழுத்துக்களை ஆங்கில பெரிய எழுத்துக்களால் மாற்றீடு செய்யும்.

தொர்புரு அணி முக்கியமாக அணியிலுள்ள தரவை கண்டுபிடித்து கையாளுகிறது அல்லது அணியிலுள்ள கூறுகளை வரைபடமாக்குகிறது   ரூபியில் தொர்புரு அணியுடன் ஒரு அணியை  நிரந்தரமாக மாற்றுவதற்கு, ஏற்கனவே உள்ள வரிசைக்கு ஒரு ஆச்சரிய குறியை சேர்க்கவும் .

animals = ["dog","cat","snake","mouse"]
animals.map! { |animal| animal.capitalize } => ["Dog", "Cat", "Snake", "Mouse"]

Animals => ["Dog", "Cat", "Snake", "Mouse"]

இந்த நேரத்தில் நிரலாக்க மொழிகளில் இரண்டு அடிப்படை சேகரிப்புகளை நீங்கள் புரிந்துகொள்கிறீர்கள்.  Enumerable தொகுதியை கற்றுக்கொண்டதன் பின்னர் அணிகள்  மற்றும் எண்ணிம அடைவு கொண்ட சேகரிப்புகளுக்கு பொதுவாக நான்கு முறைகள் பயன்படுத்தப்படும் அவை each, each_with_index, select and map

இப்போது சில உதாரணங்களோடு உங்களது அறிவை மேம்படுத்த சில பயிற்சிகளை மேற்க்கொள்ளலாம்.



