class Node
  attr_accessor :value, :left, :right

  def initialize(value, left = nil, right = nil)
    @value = value
    @left = left
    @right = right
  end

  def insert(value)
    if value < @value
      if @left.nil?
        @left = Node.new(value)
      else
        @left.insert(value)
      end
    elsif value > @value
      if @right.nil?
        @right = Node.new(value)
      else
        @right.inse(value)
      end
    end
  end

  def find(value)
    return self if value == @value

    if value > @value && !@right.nil?
      @right.find(value)
    elsif value < @value && !@left.nil?
      @left.find(value)
    else
      nil
    end
  end
end

root = Node.new(5)
root.insert(3)
root.insert(7)
root.insert(4)

found_node = root.find(4)
puts found_node.value

not_found_node = root.find(10)
puts not_found_node.nil?
