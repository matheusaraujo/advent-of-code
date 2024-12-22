use strict;
use warnings;
use Readonly;

Readonly my $MODULO => 16_777_216;

sub part2 {
    my @puzzle_input = @_;
    my %sequences    = ();

    for my $secret (@puzzle_input) {
        my @changes    = ();
        my %seen       = ();
        my $last_digit = $secret % 10;

        for ( 1 .. 2000 ) {
            $secret = ( $secret ^ ( $secret << 6 ) ) % $MODULO;
            $secret = ( $secret ^ ( $secret >> 5 ) ) % $MODULO;
            $secret = ( $secret ^ ( $secret << 11 ) ) % $MODULO;
            my $price = $secret % 10;
            my $diff  = $price - $last_digit;
            $last_digit = $price;
            push @changes, $diff;
            if ( scalar @changes >= 4 ) {
                my @seq     = @changes[ -4 .. -1 ];
                my $seq_key = join q{,}, @seq;
                if ( !$seen{$seq_key} ) {
                    $sequences{$seq_key} += $price;
                }
                $seen{$seq_key}++;
            }
        }

    }

    my ($most_common_value) =
      reverse sort { $sequences{$a} <=> $sequences{$b} } keys %sequences;
    return $sequences{$most_common_value};
}

1;

