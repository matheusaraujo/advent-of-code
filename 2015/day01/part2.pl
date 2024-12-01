#!/usr/bin/perl
use strict;
use warnings;

sub part2 {
    my @input = @_;
    my $floor = 0;

    for my $i ( 1 .. length $input[0] ) {
        my $char = substr $input[0], $i - 1, 1;

        if ( $char eq '(' ) {
            $floor += 1;
        }
        elsif ( $char eq ')' ) {
            $floor -= 1;
        }

        if ( $floor == -1 ) {
            return $i;
        }
    }
    return 0;
}

1;
