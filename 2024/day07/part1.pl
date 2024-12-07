#!/usr/bin/perl
use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    return solve( \@puzzle_input, [qw(+ *)] );
}

1;
