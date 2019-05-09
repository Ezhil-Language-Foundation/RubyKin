##எண்ணிம அடைவு (ஹாஸ் - Hash)

ரூபீ மொழியின் மற்றொரு தரவம்சம் _Hash_ அல்லது எண்ணிம அடைவு என்பது. இதனை தோடர்புரு அணி அல்லது உருப்படி அகராதி என்றும் (இதன் நிறுவும் வடிவமைப்பை பொருத்து) அழைக்கலாம்.
அதாவது ஒரு சொல்-பொருள் தொடர்பை எப்படி அகராதி பிரதிபலிக்கிரதோ அதேபோல் இவ்வாறான தரவமைப்புகள் அனைத்தும் ஒரு உருப்படி அதனுடன் தொடர்புடைய மதிப்பையும் கணினியில் கையாள உதவுகின்றது. அணி என்பதில் உள்ள வரிசைப்படுத்தும் குணம் இவ்வகை தோடரபுறு அணிகளில் கிடையாது - ஏனெனில் இவை சீரற்ற அமைக்கப்பட்டவை.

In hash collections, we use curly brackets `{ }` wrapped around pairs of information separated by a comma, `{ "like" => "this" }`. The item to the left of the arrow `=>` is the _key_ and its _value_ is the element on the right.

Hashes are extremely useful when we have multiple numbers of similar items in a list. For example, if you used a hash to organize your toy chest, it might look something like this:

```ruby
toy_chest = {
  "அன்னம்" => 12,
  "பொம்மை" => 5,
  "சொப்புச்சாமான்" => 514
}
```

Each of these items is located in our toy chest, and the number of them is represented in the hash. So we have three keys (sea_monkeys, dolls and legos) with their corresponding values (12, 5 and 514). To access information in this hash, we can use brackets like we did for arrays.
ண
```ruby
toy_chest["அன்னம்"]
=> 12

toy_chest["பொம்மை"]
=> 5

toy_chest["சொப்புச்சாமான்”]
=> 514
```

To add an item to our toy chest hash, we can simply use brackets in a similar way that we did above to retrieve information.

```ruby
toy_chest["விளையாட்டுப்பெட்டி"] = 7
=> 7

toy_chest
=> {"sea_monkeys" => 12, "dolls" => 5, "legos" => 514,
"விளையாட்டுப்பந்து" => 7}
```

By writing "விளையாட்டுப்பந்து" in brackets next to toy_chest, we’ve actually called a method on our hash, giving it a new key value pair of `"toy_cars" => 7`. To remove an element, we can call the `delete` method. Don’t worry too much about methods right now, we just want to show you how easy it is to handle data in your array or hash collections.

```ruby
toy_chest.delete("sea_monkeys")
=> 12

toy_chest
=> {"dolls" => 5, "legos" => 514, "toy_cars" => 7}
```
மேல்கண்டதை விட கூடுதலாக ரூபீயில் அடைவில் உருப்படிகளை சேர்க்கவும், நீக்கவும் மாற்றவும் அதிக வழிகள் உள்ளன். இவற்றை அனுகுவதற்கு முன் நிரல்பாகங்கள் (methods) என்பதைப்பற்றி பயிலவேண்டும். அடுத்துவரும் சில தொடர்புறு அணி உதாரணங்களை வசித்த பின் நீங்கள் மேற்படியாக அடுத்த பாடத்திற்கு செல்லலாம்!


<div style="height:30px;"></div>
