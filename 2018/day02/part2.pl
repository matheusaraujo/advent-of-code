#!/usr/bin/perl
use strict;
use warnings;

sub part2 {

    my @input = @_;
    my $size  = scalar @input;

    foreach my $i ( 0 .. $size - 1 ) {
        foreach my $j ( $i + 1 .. $size - 1 ) {

            my $diff = 0;
            my $common;
            foreach my $k ( 0 .. length( $input[$i] ) - 2 ) {

                if ( ( substr $input[$i], $k, 1 ) ne
                    ( substr $input[$j], $k, 1 ) )
                {
                    $diff++;
                }
                else {
                    $common .= substr $input[$i], $k, 1;
                }

            }
            if ( $diff == 1 ) {
                return $common;
            }
        }
    }

    return 'not found';
}

1;

