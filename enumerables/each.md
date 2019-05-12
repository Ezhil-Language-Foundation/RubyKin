ஓவ்வொன்றாக (Each)
==

'each' என்கின்ற நிரல்பாகம் (method) உங்களது அடைவில் உள்ள ஒவ்வொறு உருப்படியிலும் கொடுக்கப்பட்ட நிரல் துண்டினை இயக்கும். உதாரணமாக, ஒரு பொம்மை களஞ்சியத்தை அணியில் கொண்டு நிரல் எழுதினால் இவ்வாறு 'each' என்ற நிரல்பாகத்தை செயல்படுத்தலாம்: இதனை கொண்டு நமது பொம்மை அணியில் உள்ள உருப்படிகளின் பெயர்களை திரையில் இடலாம். அதாவது:

```ruby
toys = [
  "கார்",
  "பந்து",
  "வீரன் பொம்மை",
  "வீட்டு விலங்கு"
]
toys.each { |toy| puts toy }

# தற்போது ஒவ்வொறு பொம்மையின் பெயரும் 'toys' என்ற அணியில் இருந்து திரையிடப்படும்:
  கார்
  பந்து
  வீரன் பொம்மை
  வீட்டு விலங்கு
```

Let’s dig into the each method to see what we did. Since this method belongs to the Array class, we can call it on our toys array. We then give our `each` method a block of code to be executed or carried out and performed. In this case, we are using the `puts` method. In our `|pipes|` we define a temporary variable `toy` and call the puts method on each toy that is passed to our block.

Our each method knows to look at each element (our four toys) inside the array. This is called iterating over the array. (Iterating over the array is just a fancy way of saying look at each toy in the collection). Now we store the value of each array element inside our `|pipes|` and call the puts method on each element. We could have written the same code like so:

```ruby
toys.each do |toy|
  puts toy
end
```

The curly brackets are a way of writing `do` and `end` in one line. You don’t have to use them, but it is a shortcut that you can use if you want! Either way works, and Ruby will look to execute the code inside of our `do end` or `{ }` block. Now, let’s look at how we might use the each method on a hash.

Imagine we had more than one toy in our collection. (If your parents are teaching you how to code in Ruby, you probably have a lot more than one toy in your collection. Lucky you!) We might use a hash to better represent or organize our toy box. Using each, we can print the toy and the number of toys in our collection.

```ruby
toys = {"car" => 1, "ball" => 3, "action figure" => 2,
"stuffed animal" => 8}
toys.each { |key, value| puts "#{key} => #{value}" }

car => 1
ball => 3
action figure => 2
stuffed animal => 8
```

When using the each method on a hash, Ruby knows that each element in the array has a key and a value. We could have used anything in our `|pipes|` to name our key and value pairs ( such as `|x, y|` ), but it’s easier to read when we identify our key and value by their names. We then call the puts method again on each element, use our friend interpolation `#{ }` to place our variable values in our string, and finally put the string of the toy, and number of toys, to the screen.

<div style="height:30px;"></div>
