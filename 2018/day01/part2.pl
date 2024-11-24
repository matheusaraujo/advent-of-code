#!/usr/bin/perl
use strict;
use warnings;

sub part2 {
    my @input   = @_;
    my $result  = 0;
    my %history = ( 0 => 1 );

    while (1) {
        for my $line (@input) {
            if ( $line =~ /^[+]/smx ) {
                $result += substr $line, 1;
            }
            else {
                $result -= substr $line, 1;
            }

            if ( exists $history{$result} ) {
                return $result;
            }
            $history{$result} = 1;
        }
    }

    return -1;
}

1;

