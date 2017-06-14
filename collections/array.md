
##அணிகள்

அணி, அல்லது அணிகள், என்பது வரிசைப்படுத்தப்பட்ட, இடம் வழி அணுகும் வகை தரவமைப்புகள்; இது போன்ற அணிகளில் எந்த வகை தரவுகளையும் சேர்க்கலாம். இவைகளை வரிசைப்படுத்தலாம் என்றல் இதுவே பொருள்: பள்ளியில் காலை கூட்டத்தின் பின்பு வயது அல்லது பெயர் அகரமுதலி வரிசையில் நின்று வகுப்பறையில் நுழைவீர்கள். அணிகளும் அது போலவே. உங்கள் பள்ளி வகுப்பு மாணவர்களை வயது, பெயர், இடை, உயரம் என்ற அம்சங்களால் வரிசைப்படுத்தலாம். அதாவது இந்த நன்கு அம்சங்களில் ஏதேனும் ஒரு வகை இதனை கொண்டு வரிசைப்படுத்தலாம். இதனை நிரல் என்று எழுதினால், அது 'அணிகள்' என்பதால் குறிக்கப்படும்.

வரிசையில நாலு பிள்ளைகள் இருங்காங்க என்று கொள்ளவோம்: குமரன், முகிலன், செல்வி, மட்டும் யாழினி. நம்ம இந்த குழந்தைகளின் பெயரை எழுதியபடியே 
 இவற்றை இடம் சூட்டும் படி எண் இடலாம்.
 இப்போது குமரன் 1. முகிலன் 2. செல்வி 3. யாழினி 4.
 இந்த நாலு பிள்ளைகளும் வரிசையில் நிக்க இதையே அணியில் குறியீட்டால் 
இப்படி எழுதலாம் 
```ruby
 [‘குமரன்’, ‘செல்வி’, ‘முகிலன்’, ‘யாழினி’]
```
Arrays are noted using square brackets, with elements separated by a comma. So an array is in order, and it is also indexed. When a collection is indexed, it means that each item has a specific number that relates to its order in line. The tricky part to remember is that computers start their index at zero. This means that Adam’s index is 0, Billy is 1, Molly is 2 and Sally is 3.

One way to think about indexes is distance. Adam is first in the array, so he is zero units away from himself. Billy is next, only 1 unit away from Adam. Molly is 2 units away, and Sally is 3 units away from Adam. You could also think of array indexes like a number line, which also starts at zero.

Here’s what our array looks like with its index.

```ruby
kids_array = [‘குமரன்’, ‘செல்வி’, ‘முகிலன்’, ‘யாழினி’]
# kids_array index => [0,1,2,3]
```

If we want the first element in our ordered array, we look it up by the first index. The first index in any array is zero. We can find an element by its index using the `[ ]` method.

```ruby
kids_array[0]
=> "Adam"
```

You can think of the brackets like big monkey paws, they clamp down on both sides of the element (whatever the object) and hold it. If you type `kids_array[0]` you are asking Ruby to get the first spot. In this case, Ruby would tell you that Adam is at index zero.

We can also use the `[ ]` method to add or change an element in our array. For example, if Sally left to another school and Terry replaced her spot, we could remove Sally and replace her with Terry by using the `[ ]` method on the correct index number.

```ruby
kids_array = ["Adam", "Billy", "Molly", "Sally"]
kids_array[3] = "Terry"
kids_array
=> ["Adam", "Billy", "Molly", "Terry"]
```

இவர்களை அகரமுதலி படி  வரிசைப்படுத்தலாம். இது ‘குமரன்’, ‘செல்வி’, ‘முகிலன்’, ‘யாழினி’ என்ற வரிசையில் வரும்.

We can even add a new member to our array, like so.

```ruby
kids_array[4] = "Zoe"
kids_array
=> ["Adam", "Billy", "Molly", "Terry", "Zoe"]
```

Arrays can contain numbers, strings and even other arrays!

```ruby
number_array = [1,2,3,4,5]
string_array = ["Frank", "Suzy", "Doug", "Jane"]
mixed_array = [number_array, "a string", 13]
```

If we had an array _inside_ another array, we can use the square brackets in a similar way to access our data. In the example below, in order to grab the number 3, we use square brackets to access the first element in our array (which is another array). We then use another bracket to access the number three, the second element in that array.

```ruby
lots_of_arrays = [[1,2],"string","test"]
lots_of_arrays[0][1]
=> 2
```

Ruby gives us some cool methods to call on arrays, like `sort`. When we call the sort method on our string_array, Ruby sorts our array alphabetically. In Ruby, whenever we use the sort method, the computer understands we want to see the entire array alphabetized.

```ruby
string_array.sort
=> ["Doug", "Frank", "Jane", "Suzy"]
```

However, unless we call `sort!` on the array, the order will not change permanently and our array will stay in its original state. When we ask to sort without an exclamation mark, only the result is sorted (not the actual array). When we call `sort!` with the exclamation mark, the _actual_ array is sorted in the new alphabetized order.

```ruby
string_array
=> ["Frank", "Suzy", "Doug", "Jane"]

string_array.sort!
=> ["Doug", "Frank", "Jane", "Suzy"]
```

Before we get into more examples about arrays, it’s important to mention one of Ruby’s widely used array methods--the shovel. The shovel is written with two less-than symbols `<<` that are used to insert items to the end of an array. Let’s take the example above and add Bill to our string array.

```ruby
string_array
=> ["Doug", "Frank", "Jane", "Suzy"]
string_array << "Bill"
=> ["Doug", "Frank", "Jane", "Suzy", "Bill"]
```

We could have added Bill with the push method as well.

```ruby
string_array.push("Bill")
=> ["Doug", "Frank", "Jane", "Suzy", "Bill"]
```

The shovel method is favored by Rubyists and it’s good to know how it works. More examples on arrays below.

<div style="height:30px;"></div>
