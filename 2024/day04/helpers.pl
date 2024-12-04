#!/usr/bin/perl
use strict;
use warnings;

sub parse_input {
    my @lines = @_;
    chomp @lines;
    return map { [ split //sm ] } @lines;
}

1;
