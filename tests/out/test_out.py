def test_write_bed(chip_10, tmp_path):

    outfile = tmp_path / "deleteme.bed"
    chip_10.out.bed(outfile)


def test_write_bed_no_path(chip_10):

    result = chip_10.out.bed()
    assert isinstance(result, str)


def test_write_gtf(chip_10, tmp_path):

    outfile = tmp_path / "deleteme.gtf"
    chip_10.out.gtf(outfile)


def test_write_gtf_no_path(chip_10):

    result = chip_10.out.gtf()
    assert isinstance(result, str)


def test_write_bigwig(chip_10, tmp_path, chromsizes):

    outfile = tmp_path / "deleteme.bigwig"
    outpath = str(outfile)
    chip_10.out.bigwig(outpath, chromosome_sizes=chromsizes)
