use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;

    for my $line (@puzzle_input) {
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
