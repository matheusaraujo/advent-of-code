#!/usr/bin/perl
use strict;
use warnings;

use feature 'say';

sub part1 {
    my @input  = @_;
    my $result = 0;

    for my $line (@input) {
        if ( $line =~ /^[+]/smx ) {
            $result += substr $line, 1;
        }
        else {
            $result -= substr $line, 1;
        }
    }

    return $result;
}

1;
