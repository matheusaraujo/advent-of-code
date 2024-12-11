use strict;
use warnings;

use List::Util 'any';

sub solve {
    my ( $part, @puzzle_input ) = @_;
    my $result = 0;
    my $rules  = 0;
    my %before = ();
    my %after  = ();

    for my $line (@puzzle_input) {
        if ( $line eq q{} ) {
            last;
        }
        my @pages = split /[|]/sxm, $line;
        push @{ $before{ $pages[0] } }, $pages[1];
        push @{ $after{ $pages[1] } },  $pages[0];
        $rules++;
    }

    for my $i ( $rules + 1 .. $#puzzle_input ) {
        my $line  = $puzzle_input[$i];
        my @pages = split /,/sxm, $line;

        my @sorted_pages =
          sort {    ## no critic (BuiltinFunctions::ProhibitReverseSortBlock)
            return ( any { $a eq $_ } @{ $before{$b} } )
              || ( any { $b eq $_ } @{ $after{$a} } )
              ? 1
              : -1;
          } @pages;

        my $sorted = 1;
        for my $i ( 0 .. $#sorted_pages ) {
            if ( $sorted_pages[$i] ne $pages[$i] ) {
                $sorted = 0;
                last;
            }
        }

        if ( $sorted == 1 && $part eq 'part1' ) {
            $result += $pages[ ( scalar @pages / 2 ) ];
        }
        elsif ( $sorted == 0 && $part eq 'part2' ) {
            $result += $sorted_pages[ ( scalar @sorted_pages / 2 ) ];
        }
    }

    return $result;
}

1;
