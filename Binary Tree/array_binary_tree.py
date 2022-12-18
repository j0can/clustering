# Anna Friebe for DVA245 at MDH based on material fron Goldwasser
# with the following copyright
#
# TODO: Implement the ArrayBinaryTree and the internal Position
# class
# The element values of the tree shall be stored in a list.
# The root can be positioned at element with index 0 or 1.
# If the root is at index 0, the children of a parent are at indices 
# parentPos*2 + 1 and parentPos*2+2. The parent of a child is at (childPos - 1)/2
# If the root is at index 1, the children are at indices parentPos*2
# and parentPos*2 + 1. The parent of a child is at childPos/2
# 
#  You can look at the LinkedBinaryTree implementation in chapter 8 of
# https://github.com/mjwestcott/Goodrich
# to see similar concepts for a linked binary tree.
# 
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from binary_tree import BinaryTree

class ArrayBinaryTree(BinaryTree):
      
  """List representation of a binary tree structure."""
  class _Node:
    __slots__='_parent', '_element','_right','_left'
    def __init__(self, element, parent=None, right=None, left=None,):
      self._parent = parent
      self._element = element
      self._right = right
      self._left = left
      

  #-------------------------- nested Position class --------------------------
  class Position(BinaryTree.Position):
    """An abstraction representing the location of a single element."""
    # TODO: Implement the Position constructor
    # What information does the Position instance need to store to be able
    # to return the corresponding element and check for equality with another 
    # Position instance?
    def __init__(self, container, node):
      self._container=container
      self._node=node

    # TODO: Implement a function that returns the element at the Position
    # instance
    def element(self):
      return self._node._element
    # TODO: Implement a function that checks if the Position instance refers 
    # to the same location of the same tree as the Position given in the "other" 
    # parameter
    def __eq__(self, other):
      return type(other) is type(self) and other._node is self._node

  #------------------------------- utility methods -------------------------------
  # TODO Complete the _validate function: check that p belongs to this 
  # ArrayBinaryTree instance, and return the array index of p if valid
  def _validate(self, p):
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._parent is p._node:
      raise ValueError('p is no longer valid')
    return p._node
  # TODO: Implement a function that creates and returns a Position instance for 
  # the arrayIndex location if the index is within the list size and 
  # contains an element. Otherwise return None.
  def _make_position(self, arrayIndex):
    return self.Position(self, arrayIndex) if arrayIndex is not None else None
  #-------------------------- array binary tree constructor --------------------------
  # TODO: Implement a constructor that creates a list of a fixed length (512) to hold
  # the elements of the tree. All elements in the list hold None at construction.
  def __init__(self):
    self._root = None
    self._size = 0

  #-------------------------- public accessors --------------------------
  # TODO: Implement the len() operator that returns the total number of elements
  # in the tree.
  def __len__(self):
    return self._size
  
  # TODO: Implement the root function from the Tree base class.
  # Return the root Position of the tree. Use _make_position.
  def root(self):
    return self._make_position(self._root)

  # TODO: Implement the parent function from the Tree base class.
  # Return the Position of p's parent. Use _validate and _make_position.
  def parent(self, p):
    node = self._validate(p)
    return self._make_position(node._parent)
  # TODO: Implement the left function from the BinaryTree base class.
  # Return the Position of p's left child. Use _validate and _make_position.
  def left(self, p):
    node = self._validate(p)
    return self._make_position(node._left)

  # TODO: Implement the right function from the BinaryTree base class.
  # Return the Position of p's right child. Use _validate and _make_position.
  def right(self, p):
    node = self._validate(p)
    return self._make_position(node._right)

  # TODO: Implement the num_children function from the Tree base class.
  # Return the number of children of p. Use _validate.
  def num_children(self, p):
    node = self._validate(p)
    count = 0
    if node._left is not None:
      count += 1
    if node._right is not None:
      count += 1
    return count

  #-------------------------- nonpublic mutators --------------------------
  # TODO: Implement a function that places the element e at the root 
  # of an empty tree and returns the Position of the root.
  def _add_root(self, e):
    if self._root is not None:
      raise ValueError('root exists')
    self._size =1
    self._root = self._Node(e)
    return self._make_position(self._root)

  # TODO: implement a function that places the element e in the left child of
  # p and returns the Position of the child.
  def _add_left(self, p, e):
    node = self._validate(p)
    if node._left is not None:
      raise ValueError('Left child exists')
    self._size += 1
    node._left = self._Node(e, node)
    return self._make_position(node._left)


  # TODO: implement a function that places the element e in the right child of
  # p and returns the Position of the child.
  def _add_right(self, p, e):
    node= self._validate(p)
    if node._right is not None:
      raise ValueError('Right child exists')
    self._size +=1
    node._right = self._Node(e, node)
    return self._make_position(node._right)