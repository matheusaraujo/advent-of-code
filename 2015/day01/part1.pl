#!/usr/bin/perl
use strict;
use warnings;

sub part1 {
    my @input  = @_;
    my $result = 0;

    $result = ( ( $input[0] =~ tr/(// ) ) - ( $input[0] =~ tr/)// );

    return $result;
}

1;
