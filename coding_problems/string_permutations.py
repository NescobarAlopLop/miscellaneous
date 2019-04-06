import unittest


def permutation(s1: str, s2: str) -> bool:
	if len(s1) != len(s2):
		return False
	char_counter = [0] * 256  # assumption
	for c in s1:
		char_counter[ord(c)] += 1
	for c in s2:
		char_counter[ord(c)] -= 1
	for c in char_counter:
		if c != 0:
			return False
	return True


def permutation_sorted(s1: str, s2: str) -> bool:
	if len(s1) != len(s2): return False
	for (c1, c2) in zip(sorted(s1), sorted(s2)):
		if c1 != c2:
			return False
	return True


class TestSolution(unittest.TestCase):

	def test_permutation_test_positive(self):
		self.assertTrue(permutation('abcd', 'badc'))
		self.assertTrue(permutation('abcd', 'badc'))
		self.assertTrue(permutation('aaaa', 'aaaa'))

	def test_permutation_test_negative(self):
		self.assertFalse(permutation('asbcd', 'badc'))
		self.assertFalse(permutation('aaaab', 'baaab'))

	def test_permutation_sorted_test_true(self):
		self.assertTrue(permutation_sorted('abcd', 'badc'))
		self.assertTrue(permutation_sorted('aaaa', 'aaaa'))

	def test_permutation_sorted_test_false(self):
		self.assertFalse(permutation_sorted('asbcd', 'badc'))
		self.assertFalse(permutation('aaaab', 'baaab'))


if __name__ == '__main__':
	unittest.main()
