"""
Tests for subset_fontsize parameter in venn2 and venn3.

Copyright 2024, Konstantin Tretyakov.
http://kt.era.ee/

Licensed under MIT license.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib_venn as mv


def test_venn2_subset_fontsize_default():
    """Test that venn2 subset labels have default fontsize when not specified"""
    v = mv.venn2(subsets=(1, 2, 3))
    for label_id in ['10', '01', '11']:
        label = v.get_label_by_id(label_id)
        if label:
            # Default matplotlib fontsize is 10.0
            assert label.get_fontsize() == 10.0, f"Expected default fontsize 10.0, got {label.get_fontsize()}"


def test_venn2_subset_fontsize_custom():
    """Test that venn2 subset labels respect custom fontsize"""
    fontsize = 16.0
    v = mv.venn2(subsets=(1, 2, 3), subset_fontsize=fontsize)
    for label_id in ['10', '01', '11']:
        label = v.get_label_by_id(label_id)
        if label:
            assert label.get_fontsize() == fontsize, f"Expected fontsize {fontsize}, got {label.get_fontsize()}"


def test_venn3_subset_fontsize_default():
    """Test that venn3 subset labels have default fontsize when not specified"""
    v = mv.venn3(subsets=(1, 1, 1, 1, 1, 1, 1))
    for label_id in ['100', '010', '110', '001', '101', '011', '111']:
        label = v.get_label_by_id(label_id)
        if label:
            # Default matplotlib fontsize is 10.0
            assert label.get_fontsize() == 10.0, f"Expected default fontsize 10.0, got {label.get_fontsize()}"


def test_venn3_subset_fontsize_custom():
    """Test that venn3 subset labels respect custom fontsize"""
    fontsize = 18.0
    v = mv.venn3(subsets=(1, 1, 1, 1, 1, 1, 1), subset_fontsize=fontsize)
    for label_id in ['100', '010', '110', '001', '101', '011', '111']:
        label = v.get_label_by_id(label_id)
        if label:
            assert label.get_fontsize() == fontsize, f"Expected fontsize {fontsize}, got {label.get_fontsize()}"


def test_venn2_subset_fontsize_with_dict_input():
    """Test that subset_fontsize works with dict input"""
    fontsize = 15.0
    v = mv.venn2(subsets={'10': 1, '01': 2, '11': 3}, subset_fontsize=fontsize)
    for label_id in ['10', '01', '11']:
        label = v.get_label_by_id(label_id)
        if label:
            assert label.get_fontsize() == fontsize, f"Expected fontsize {fontsize}, got {label.get_fontsize()}"


def test_venn3_subset_fontsize_with_dict_input():
    """Test that subset_fontsize works with dict input"""
    fontsize = 17.0
    v = mv.venn3(
        subsets={'100': 1, '010': 1, '110': 1, '001': 1, '101': 1, '011': 1, '111': 1},
        subset_fontsize=fontsize
    )
    for label_id in ['100', '010', '110', '001', '101', '011', '111']:
        label = v.get_label_by_id(label_id)
        if label:
            assert label.get_fontsize() == fontsize, f"Expected fontsize {fontsize}, got {label.get_fontsize()}"


def test_venn2_set_labels_unaffected():
    """Test that set labels (A, B) are not affected by subset_fontsize"""
    subset_fontsize = 20.0
    v = mv.venn2(subsets=(1, 2, 3), set_labels=('A', 'B'), subset_fontsize=subset_fontsize)
    
    # Subset labels should have the custom fontsize
    assert v.get_label_by_id('10').get_fontsize() == subset_fontsize
    
    # Set labels should still have their default "large" size (12.0)
    assert v.get_label_by_id('A').get_fontsize() == 12.0
    assert v.get_label_by_id('B').get_fontsize() == 12.0


def test_venn3_set_labels_unaffected():
    """Test that set labels (A, B, C) are not affected by subset_fontsize"""
    subset_fontsize = 20.0
    v = mv.venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('A', 'B', 'C'), subset_fontsize=subset_fontsize)
    
    # Subset labels should have the custom fontsize
    assert v.get_label_by_id('100').get_fontsize() == subset_fontsize
    
    # Set labels should still have their default "large" size (12.0)
    assert v.get_label_by_id('A').get_fontsize() == 12.0
    assert v.get_label_by_id('B').get_fontsize() == 12.0
    assert v.get_label_by_id('C').get_fontsize() == 12.0
