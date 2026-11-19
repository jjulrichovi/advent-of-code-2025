from aoclib.grid import browse_all, manhattan, neighbors
from aoclib.io import read_grid, read_ints, read_lines
from aoclib.parsing import ints, paragraphs


def test_ints():
    assert ints("a 1, -2 x3") == [1, -2, 3]


def test_paragraphs():
    assert paragraphs("a\nb\n\nc\n") == ["a\nb", "c"]


def test_browse_all():
    assert list(browse_all(["ab", "cd"])) == [(0, 0), (0, 1), (1, 0), (1, 1)]


def test_manhattan():
    assert manhattan((0, 0), (-2, 3)) == 5


def test_neighbors_corner():
    assert sorted(neighbors((0, 0), 3, 3)) == [(0, 1), (1, 0)]
    assert len(list(neighbors((1, 1), 3, 3, diagonal=True))) == 8


def test_io(tmp_path):
    f = tmp_path / "in.txt"
    f.write_text("1\n2\n3\n")
    assert read_lines(f) == ["1", "2", "3"]
    assert read_ints(f) == [1, 2, 3]
    assert read_grid(f) == [["1"], ["2"], ["3"]]
