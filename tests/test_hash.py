from lumix.hash.convert import compute_hash


def test_compute_hash():
    assert compute_hash("hello world", "sha256") == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    assert compute_hash("ciao", "md5") == "6e6bc4e49dd477ebc98ef4046c067b5f"
