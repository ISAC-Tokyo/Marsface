class AddNumToVotes < ActiveRecord::Migration
  def change
    add_column :votes, :num, :integer
  end
end
