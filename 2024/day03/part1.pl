use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 0;

    foreach my $line (@puzzle_input) {
        my @matches = $line =~ /mul[(](\d+),(\d+)[)]/sxmg;
        while (@matches) {
            my $a = shift @matches;
            my $b = shift @matches;
            $result += $a * $b;
        }
    }

    return $result;
}

1;
