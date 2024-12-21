# TODO: @matheusaraujo, this code needs to be refactored

## no critic (BuiltinFunctions::ProhibitUselessTopic)
## no critic (ControlStructures::ProhibitPostfixControls)
## no critic (RegularExpressions::RequireDotMatchAnything)
## no critic (RegularExpressions::RequireExtendedFormatting)
## no critic (RegularExpressions::RequireLineBoundaryMatching)
## no critic (ValuesAndExpressions::ProhibitEmptyQuotes)
## no critic (ValuesAndExpressions::ProhibitNoisyQuotes)

use strict;
use warnings;

my %numeric_keypad = (

    # Original numeric_keypad
    '0,0' => '7',
    '0,1' => '8',
    '0,2' => '9',
    '1,0' => '4',
    '1,1' => '5',
    '1,2' => '6',
    '2,0' => '1',
    '2,1' => '2',
    '2,2' => '3',
    '3,1' => '0',
    '3,2' => 'A',

    # Reversed numeric_keypad
    '7' => '0,0',
    '8' => '0,1',
    '9' => '0,2',
    '4' => '1,0',
    '5' => '1,1',
    '6' => '1,2',
    '1' => '2,0',
    '2' => '2,1',
    '3' => '2,2',
    '0' => '3,1',
    'A' => '3,2',
);
my %directional_keypad = (

    # Original directional_keypad
    '0,1' => '^',
    '0,2' => 'A',
    '1,0' => '<',
    '1,1' => 'v',
    '1,2' => '>',

    # Reversed directional_keypad
    '^' => '0,1',
    'A' => '0,2',
    '<' => '1,0',
    'v' => '1,1',
    '>' => '1,2',
);

sub move_numeric_keypad {
    my $path = shift;
    return move( $path, \%numeric_keypad );
}

sub move_directional_keypad {
    my $path = shift;
    return move( $path, \%directional_keypad );
}

sub move {
    my ( $path, $pad ) = @_;
    my @output = ();
    my $start  = 'A';
    for my $end ( split //, $path ) {
        push @output, step( $start, $end, $pad );
        $start = $end;
    }
    return join '', @output;
}

sub move_part2 {
    my $path  = shift;
    my %out   = ();
    my $start = 'A';

    for my $end ( split //, $path ) {
        $out{ step( $start, $end, \%directional_keypad ) }++;
        $start = $end;
    }

    return \%out;
}

sub route_length {
    my ($route) = @_;
    my $len = 0;
    $len += length($_) * $route->{$_} for keys %{$route};
    return $len;
}

sub step {
    my ( $source, $target, $pad ) = @_;
    my ( $ti,     $tj ) = split /,/, $pad->{$target};
    my ( $si,     $sj ) = split /,/, $pad->{$source};
    my $di    = $ti - $si;
    my $dj    = $tj - $sj;
    my $vert  = ( $di > 0 ? 'v' x $di : '^' x -$di );
    my $horiz = ( $dj > 0 ? '>' x $dj : '<' x -$dj );

    if ( $dj > 0 && exists $pad->{"$ti,$sj"} ) {
        return $vert . $horiz . 'A';
    }
    if ( exists $pad->{"$si,$tj"} ) {
        return $horiz . $vert . 'A';
    }
    if ( exists $pad->{"$ti,$sj"} ) {
        return $vert . $horiz . 'A';
    }
    return '';
}

1;
