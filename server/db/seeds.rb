# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
Image.delete_all
Vote.delete_all
Dir.foreach('app/assets/images/targets') do |item|
  next if (item == '.' || item == '..')
  puts 'load:' + item
  Image.create(:caption => item, :path => '/assets/targets/' + item)
end
