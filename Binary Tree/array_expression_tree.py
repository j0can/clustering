
from array_binary_tree import ArrayBinaryTree
from testReport import testReport

class ArrayExpressionTree(ArrayBinaryTree):
  """An arithmetic expression tree."""


  def __init__(self, prefixExpression):
    """Create an expression tree.

    prefixExpression should be a binary expression tree as a list in prefix format, 
    such as ['+', '2', '45'] representing 2+45
    or ['-', '*', '4', '/', '6', '3','+', '-', '7', '2', '6'] representing (4*(6/3))-((7-2)+6)
    operators '+', '-', '/' and '*' or equivalently 'x' are allowed
    """
    super().__init__()                        # ListBinaryTree initialization
    rootPos = self._add_root(prefixExpression[0])                     # use inherited, nonpublic method
    self._recursiveAddFromPrefixExpression(rootPos, prefixExpression[1:len(prefixExpression)])
    

  def __str__(self):
    """Return string representation of the expression."""
    pieces = []                 # sequence of piecewise strings to compose
    self._parenthesize_recur(self.root(), pieces)
    return ''.join(pieces)

  def _parenthesize_recur(self, p, result):
    """Append piecewise representation of p's subtree to resulting list."""
    if self.is_leaf(p):
      result.append(str(p.element()))                    # leaf value as a string
    else:
      result.append('(')                                 # opening parenthesis
      self._parenthesize_recur(self.left(p), result)     # left subtree
      result.append(p.element())                         # operator
      self._parenthesize_recur(self.right(p), result)    # right subtree
      result.append(')')                                 # closing parenthesis

  def evaluate(self):
    """Return the numeric result of the expression."""
    return self._evaluate_recur(self.root())

  def _evaluate_recur(self, p):
    """Return the numeric result of subtree rooted at p."""
    if self.is_leaf(p):
      return float(p.element())      # we assume element is numeric
    else:
      op = p.element()
      left_val = self._evaluate_recur(self.left(p))
      right_val = self._evaluate_recur(self.right(p))
      if op == '+':
        return left_val + right_val
      elif op == '-':
        return left_val - right_val
      elif op == '/':
        return left_val / right_val
      else:                          # treat 'x' or '*' as multiplication
        return left_val * right_val   
      
  
  def _recursiveAddFromPrefixExpression(self, position, prefixExpression):
    SYMBOLS = set('+-x*/() ')    # allow for '*' or 'x' for multiplication
    leftPos = self._add_left(position, prefixExpression[0])
    addedOnLeft = 1
    if prefixExpression[0] in SYMBOLS:
      addedOnLeft = 1 + self._recursiveAddFromPrefixExpression(leftPos, prefixExpression[1:len(prefixExpression)])
    rightPos = self._add_right(position, prefixExpression[addedOnLeft])
    addedOnRight = 1
    if prefixExpression[addedOnLeft] in SYMBOLS:
      addedOnRight = 1 + self._recursiveAddFromPrefixExpression(rightPos, prefixExpression[addedOnLeft+1:len(prefixExpression)])
    return addedOnLeft + addedOnRight
    


if __name__ == '__main__':
  tree = ArrayExpressionTree(['*','-', '6', '4', '+', '/', '28', '2', '*', '4', '5'])
  val = tree.evaluate()
  result = ((6-4)*((28/2)+(4*5)))
  testReport(val == result, "ExpressionTree evaluate")
  testReport(str(tree) == '((6-4)*((28/2)+(4*5)))', "Expression tree string representation")
  testReport(len(tree) == 11, "len(tree)")
  tree2 = ArrayExpressionTree(['*','-', '6', '4', '+', '/', '28', '2', '*', '4', '5'])
  root1 = tree.root()
  root2 = tree.root()
  pos2 = tree.left(root1)
  testReport(tree.num_children(tree.left(pos2))==0, "Num children")
  testReport(tree.num_children(root1)==2, "Num children")
  testReport(root1 == root2, "Tree position equality")
  testReport(root1 != pos2, "Tree position inequality")
  testReport(root1 != tree2.root(), "Tree position inequality")
