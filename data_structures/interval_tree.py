# chat gpts attempt at implementing an interval tree

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other):
        return self.start <= other.end and self.end >= other.start

    def __repr__(self):
        return f"Interval({self.start}, {self.end})"


class IntervalNode:
    def __init__(self, interval):
        self.interval = interval
        self.max_end = interval.end
        self.left = None
        self.right = None


class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        self.root = self._insert(self.root, interval)

    def _insert(self, node, interval):
        if node is None:
            return IntervalNode(interval)

        # Left or right subtree?
        if interval.start < node.interval.start:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)

        # Update the max_end value
        if node.max_end < interval.end:
            node.max_end = interval.end

        return node

    def search_overlapping(self, interval):
        return self._search_overlapping(self.root, interval)

    def _search_overlapping(self, node, interval):
        results = []
        if node is None:
            return results

        # If there's any overlap, add the node's interval to the results
        if node.interval.overlaps(interval):
            results.append(node.interval)

        # Explore left subtree if it might contain overlapping intervals
        if node.left and node.left.max_end >= interval.start:
            results.extend(self._search_overlapping(node.left, interval))

        # Explore right subtree if it might contain overlapping intervals
        if node.right and interval.end >= node.interval.start:
            results.extend(self._search_overlapping(node.right, interval))

        return results

    # Placeholder for deletion operation
    def delete(self, interval):
        # Implement deletion logic here
        pass


# Example usage
if __name__ == "__main__":
    intervals = [
        Interval(15, 20),
        Interval(10, 30),
        Interval(17, 19),
        Interval(5, 20),
        Interval(12, 15),
        Interval(30, 40),
    ]
    tree = IntervalTree()
    for interval in intervals:
        tree.insert(interval)

    search_interval = Interval(6, 7)
    print(
        f"Overlapping intervals with {search_interval}:",
        tree.search_overlapping(search_interval),
    )
