"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"8","name":"flipper","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":0},{"hwid":"9","name":"flywheel","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":1},{"hwid":"10","name":"flywheel_2","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":2},{"hwid":"11","name":"rightFront","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":3},{"hwid":"12","name":"rightBack","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":4},{"hwid":"13","name":"leftFront","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":5},{"hwid":"14","name":"intake","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":6},{"hwid":"15","name":"leftBack","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":7},{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":8},{"hwid":"drivetrain","name":"DRC","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"11","rightMotorHwId":"20","wheelTravel":319.1764,"trackWidth":292.1},"bufferIndex":9},{"hwid":"controller","name":"DRC_Controler","typeName":"controller_one","extraConfig":null,"bufferIndex":10},{"hwid":"Axis1","name":"axis1","typeName":"controller_axis","extraConfig":null,"bufferIndex":11},{"hwid":"Axis2","name":"axis2","typeName":"controller_axis","extraConfig":null,"bufferIndex":12},{"hwid":"Axis3","name":"axis3","typeName":"controller_axis","extraConfig":null,"bufferIndex":13},{"hwid":"Axis4","name":"axis4","typeName":"controller_axis","extraConfig":null,"bufferIndex":14},{"hwid":"ButtonL1","name":"buttonL1","typeName":"controller_button","extraConfig":null,"bufferIndex":15},{"hwid":"ButtonL2","name":"buttonL2","typeName":"controller_button","extraConfig":null,"bufferIndex":16},{"hwid":"ButtonR1","name":"buttonR1","typeName":"controller_button","extraConfig":null,"bufferIndex":17},{"hwid":"ButtonR2","name":"buttonR2","typeName":"controller_button","extraConfig":null,"bufferIndex":18},{"hwid":"ButtonUp","name":"buttonUp","typeName":"controller_button","extraConfig":null,"bufferIndex":19},{"hwid":"ButtonDown","name":"buttonDown","typeName":"controller_button","extraConfig":null,"bufferIndex":20},{"hwid":"ButtonLeft","name":"buttonLeft","typeName":"controller_button","extraConfig":null,"bufferIndex":21},{"hwid":"ButtonRight","name":"buttonRight","typeName":"controller_button","extraConfig":null,"bufferIndex":22},{"hwid":"ButtonX","name":"buttonX","typeName":"controller_button","extraConfig":null,"bufferIndex":23},{"hwid":"ButtonB","name":"buttonB","typeName":"controller_button","extraConfig":null,"bufferIndex":24},{"hwid":"ButtonY","name":"buttonY","typeName":"controller_button","extraConfig":null,"bufferIndex":25},{"hwid":"ButtonA","name":"buttonA","typeName":"controller_button","extraConfig":null,"bufferIndex":26}]}"""
"""__BLOCKLY__
<xml xmlns="http://www.w3.org/1999/xhtml"><block type="procedures_defnoreturn" id="!Fu=)cfMVTDEPrhZQ;M[" x="588" y="-170"><field name="NAME">flyWheelControl</field><statement name="STACK"><block type="controls_if" id="WcNUrBCS`+~=2@0Jz2a^"><value name="IF0"><block type="vexv5_controller_button_pressing" id="ew%`5BSA9hk:15I[b3dH"><field name="WIDGET_ID">ButtonX</field></block></value><statement name="DO0"><block type="variables_set" id="dJe#R!Sx]dB[W_caUT86"><field name="VAR">on</field><value name="VALUE"><block type="math_arithmetic" id="/!3;Dn`;H?,,kaR^)6jF"><field name="OP">MULTIPLY</field><value name="A"><block type="variables_get" id="4tU`Ru0kQ;6NbA#JYx4;"><field name="VAR">on</field></block></value><value name="B"><block type="math_number" id="Jjk6W][/,5BLLkHOTHr1"><field name="NUM">-1</field></block></value></block></value><next><block type="sleep" id="(8JhzU_PEyW6waJ2?aoB"><value name="seconds"><block type="math_number" id="_FM6eRf?j]w-k1,c~YsE"><field name="NUM">0.3</field></block></value></block></next></block></statement><next><block type="controls_if" id="ogercc)`@[q:Std:XoG)"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="6[XNH}]I{C)vC)r7N-)@"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="Wxz^NR)9I0I^Zt^olouZ"><field name="VAR">on</field></block></value><value name="B"><block type="math_number" id="+kqhREJjMwz~~%V%@nu*"><field name="NUM">-1</field></block></value></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="M7v,i|Bhj:)0JteBwze^"><field name="WIDGET_ID">18</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="%5ftboWW-fRsRuo1HqMt"><field name="NUM">100</field></block></value><next><block type="vexv5_motor_spin" id="JCxclH)jK@1*UV4V`v?m"><field name="WIDGET_ID">13</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="7xvqY?ZN?.loo67,5+,f"><field name="NUM">100</field></block></value></block></next></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="Cj*@4IRx0jkdE]dt^hkl"><field name="WIDGET_ID">18</field><field name="p0">COAST</field><next><block type="vexv5_motor_stop" id="0XyK.W3m8`x:(#{VRacN"><field name="WIDGET_ID">13</field><field name="p0">COAST</field></block></next></block></statement></block></next></block></statement></block><block type="procedures_defnoreturn" id="rUpS9gAb;7OYNQ}!xg6w" x="-79" y="-101"><field name="NAME">driveControl</field><statement name="STACK"><block type="controls_if" id="|-T7GE9Jv;`?-v[)y?}5"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="X}prQHkPE=#MuFpt8HSN"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="[3g:aJ6I`E9H6XFq2vVs"><field name="VAR">direction</field></block></value><value name="B"><block type="math_number" id="bJ,uL+EE%JWyl9SVoZ3h"><field name="NUM">-1</field></block></value></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="Ib!@SU[aGebSxw8BgS%`"><field name="WIDGET_ID">20</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id=",{nN@Mpi4Z2T+1-tBu.b"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="by3;J[ZcJj/heY6)wpe2"><field name="WIDGET_ID">19</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="Ej:c`;eGGN;mJnf0}z[P"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="~TxGT}Bmwibc51X@{ZLS"><field name="WIDGET_ID">11</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="#.5{Q,:%nkE!-C5lT#Aq"><field name="WIDGET_ID">Axis3</field></block></value><next><block type="vexv5_motor_spin" id="}xrH8Eg:SMg@#xM=ScQ1"><field name="WIDGET_ID">12</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="jI*NV~;3OUzMm_)NF8_;"><field name="WIDGET_ID">Axis3</field></block></value></block></next></block></next></block></next></block></statement><statement name="ELSE"><block type="vexv5_motor_spin" id="b?,)b#`7+Xc1~u=tkF7c"><field name="WIDGET_ID">12</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="!mpX%rerW).w:k)ppzV0"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="3otNKZ+,5BzV5E12YhDK"><field name="WIDGET_ID">11</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="q[0N-xHd):|fnU;_Lo;6"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="TmJ{A[e12h+^*pu91v*F"><field name="WIDGET_ID">19</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="bL|s4sUDQb7yd0(+i;^e"><field name="WIDGET_ID">Axis3</field></block></value><next><block type="vexv5_motor_spin" id="EyUpU@Rv}4Xexia|s`i~"><field name="WIDGET_ID">20</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="|oPY/;](2DWnCn~BPWp+"><field name="WIDGET_ID">Axis3</field></block></value></block></next></block></next></block></next></block></statement></block></statement></block><block type="vexv5_brain_lcd_print_line" id="#1*zYD;qa-`jhp_G0QpD" disabled="true" x="1354" y="-152"><field name="p0">1</field><value name="p1"><block type="variables_get" id="aA{[XwVEMKat*_]R2Th{"><field name="VAR">direction</field></block></value></block><block type="vexv5_start_drivercontrol" id="3" x="1119" y="-93"><next><block type="controls_forever" id="5"><statement name="DO"><block type="procedures_callnoreturn" id="9s*sBg6YV+L]I27xi1ze"><mutation name="DriverSwitch"></mutation><next><block type="procedures_callnoreturn" id="j3d,2`yJWDc7i+x+t(9~"><mutation name="ballController"></mutation><next><block type="procedures_callnoreturn" id="q-*]ME.:YaFdf9c%%_L^"><mutation name="driveControl"></mutation><next><block type="procedures_callnoreturn" id="N2%7`Lu,3y_#j98?37`;"><mutation name="flyWheelControl"></mutation><next><block type="procedures_callnoreturn" id="~8Tl_q;7BV!`l^wh`lWx"><mutation name="flipper"></mutation></block></next></block></next></block></next></block></next></block></statement></block></next></block><block type="vexv5_controller_lcd_print_at_line" id="Qu_Zh5hSyowH}0g6_R#`" disabled="true" x="1287" y="-43"><field name="WIDGET_ID">PRIMARY</field><field name="p0">1</field><value name="p1"><block type="vexv5_motor_velocity" id="q!oVCrGN@cLMmHMc,q`R"><field name="WIDGET_ID">17</field><field name="p0">RPM</field></block></value></block><block type="procedures_callnoreturn" id="|SR6qO3ckuOqZ~?`i*@E" disabled="true" x="1357" y="6"><mutation name="liftFunction"></mutation></block><block type="vexv5_start_autonomous" id="5rlEmfFO8S{^E!|?Zs`Y" disabled="true" x="1455" y="67"></block><block type="vexv5_start_autonomous" id="1" x="1627" y="60"><next><block type="variables_set" id="#3*x1RAj!kl?=+XhIqCi"><field name="VAR">on</field><value name="VALUE"><block type="math_number" id="C@PRF5Vii]EY_w-cn~0L"><field name="NUM">1</field></block></value><next><block type="variables_set" id="ypT#5^o4}uYK1hh5zJ07"><field name="VAR">direction</field><value name="VALUE"><block type="math_number" id="yh;fH|LQ#ItYdoIlO[W1"><field name="NUM">-1</field></block></value><next><block type="vexv5_drivetrain_set_velocity" id="P1v;}8kg%R3.9Q/im4sb"><field name="p1">PCT</field><value name="p0"><block type="math_number" id="ab-jZ~xWe!?cYEEHlIa;"><field name="NUM">65</field></block></value><next><block type="vexv5_motor_set_velocity" id="D%-g8/0TO{qj5D_~XALM"><field name="WIDGET_ID">16</field><field name="p1">PCT</field><value name="p0"><block type="math_number" id="44KD/`%*MA./]fW)d2Re"><field name="NUM">100</field></block></value><next><block type="vexv5_motor_spin" id="%o%V9_P8s~VN#uU0IV}}"><field name="WIDGET_ID">18</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="fsjp#s31J`dTbt78UARL"><field name="NUM">100</field></block></value><next><block type="vexv5_motor_spin" id="R*P)Gzr_hgN1dbT@|pjO"><field name="WIDGET_ID">13</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="LiNZ%;%xIjU6OB;zUSlI"><field name="NUM">100</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="%HS?R-4(7gbU5Zq8|SEX"><field name="p0">FWD</field><field name="p2">IN</field><value name="p1"><block type="math_number" id="whrS-C~0U1mOT51R:Ylg"><field name="NUM">49</field></block></value><next><block type="vexv5_motor_rotate_for_time" id="5KM6[B+%#F@EbA`TApi@"><field name="WIDGET_ID">16</field><field name="p0">FWD</field><field name="p2">SEC</field><value name="p1"><block type="math_number" id="39^@S,@]jpVe;845nTJ;"><field name="NUM">0.5</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="[6MFJ8GcfmZ???b*E{g@"><field name="p0">REV</field><field name="p2">IN</field><value name="p1"><block type="math_number" id=");qm2;X!%fhVS%K5Wd)f"><field name="NUM">35</field></block></value><next><block type="vexv5_drivetrain_turn_for" id="pmc/~[XO9Ck~/y2,jk^0"><field name="p0">RIGHT</field><field name="p2">DEG</field><value name="p1"><block type="math_number" id="]k/zwMt}VASS,!`!%lwF"><field name="NUM">100</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="IvP-G`rjjWS0Z%8ESKqz"><field name="p0">FWD</field><field name="p2">IN</field><value name="p1"><block type="math_number" id="FnL99wndf3}iS*F_*7do"><field name="NUM">22</field></block></value><next><block type="sleep" id="L1(ypGa]dpv1+ru_8x-p"><value name="seconds"><block type="math_number" id="l-Gu;NuFMkxVM^QmN0FR"><field name="NUM">1</field></block></value><next><block type="vexv5_motor_rotate_for_time" id="n!#]qD,YEJqasY1Caa##"><field name="WIDGET_ID">16</field><field name="p0">FWD</field><field name="p2">SEC</field><value name="p1"><block type="math_number" id="c[ScLPr3]0U;69kP3oLy"><field name="NUM">0.5</field></block></value><next><block type="vexv5_drivetrain_set_velocity" id="0ZHaZZ{,PT2qw2/?gTLE"><field name="p1">PCT</field><value name="p0"><block type="math_number" id="fO2e*`|R+F[fl)6UcKba"><field name="NUM">75</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="aU]^Z;xYP29Uy#~1N}zE"><field name="p0">FWD</field><field name="p2">IN</field><value name="p1"><block type="math_number" id="Q9!.Q9aj3lj4{#:v#%M_"><field name="NUM">12</field></block></value><next><block type="sleep" id="NOU4Xxmc?m75(sFg7WG*"><value name="seconds"><block type="math_number" id="L1yv14hG[QPPLF([qtCW"><field name="NUM">0.5</field></block></value><next><block type="vexv5_drivetrain_set_velocity" id="*XxbQca+b/C2F0Fe^[jZ"><field name="p1">PCT</field><value name="p0"><block type="math_number" id=",QR/|W_Lsm0jE39a}-Tn"><field name="NUM">100</field></block></value><next><block type="vexv5_motor_rotate_for_time" id="#WMBL5wBCsvA8l/H-JH="><field name="WIDGET_ID">16</field><field name="p0">FWD</field><field name="p2">SEC</field><value name="p1"><block type="math_number" id="|VL(rj?*NMB:%MoR+uLd"><field name="NUM">0.4</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="6(j9b;A0w{m3tt!EtpWc"><field name="p0">FWD</field><field name="p2">IN</field><value name="p1"><block type="math_number" id="}Brn8MciruO=U/;:LKZY"><field name="NUM">19</field></block></value></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="procedures_defnoreturn" id="oZ-r]53NJdE`OS/hw^5B" x="596" y="202"><field name="NAME">DriverSwitch</field><statement name="STACK"><block type="controls_if" id="%bnqH!RONZGKwCjgo_F%"><value name="IF0"><block type="vexv5_controller_button_pressing" id="){#YaT/.}bxsr{mg#]+4"><field name="WIDGET_ID">ButtonLeft</field></block></value><statement name="DO0"><block type="variables_set" id="7il}5+8b-1}g=F:Il2c;"><field name="VAR">direction</field><value name="VALUE"><block type="math_arithmetic" id="n*A!X,]Oa]AYV~XCLH?J"><field name="OP">MULTIPLY</field><value name="A"><block type="variables_get" id="aWz_G|a`^dsP@:Q4u?x^"><field name="VAR">direction</field></block></value><value name="B"><block type="math_number" id="pH]bI5cDIO4Xo-]t.9wz"><field name="NUM">-1</field></block></value></block></value><next><block type="sleep" id="KnaJ;(;m6Q1NMU)iCoZK"><value name="seconds"><block type="math_number" id="~Z`Y[;/@B?F-:!(?X(Tc"><field name="NUM">0.25</field></block></value></block></next></block></statement></block></statement></block><block type="procedures_defnoreturn" id="K-9)Le26Q12nPXD4~9-S" x="593" y="368"><field name="NAME">ballController</field><statement name="STACK"><block type="controls_if" id="r/WnDinTw|k@FFr`Pw1u"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="k~lowos3sGf/_SY[t@}4"><field name="WIDGET_ID">ButtonR2</field></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="NF5}M5tGYUmO.v17V@xF"><field name="WIDGET_ID">16</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="@X@u/Znyt!#`o.?@Zi5q"><field name="NUM">100</field></block></value></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="wc:H9]1McSFpTo#|jXZ/"><field name="WIDGET_ID">ButtonR1</field></block></value><statement name="DO1"><block type="vexv5_motor_spin" id="q@cO(n[t?A~lo=%CUD.N"><field name="WIDGET_ID">16</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="@/uM:y?2*vm6=*X0_0w8"><field name="NUM">100</field></block></value></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="oUDxsTsmvq`BBGM:esoN"><field name="WIDGET_ID">16</field><field name="p0">HOLD</field></block></statement></block></statement></block><block type="procedures_defnoreturn" id="g73xjS8.xy5]F1hEIKi^" disabled="true" x="1132" y="381"><field name="NAME">liftFunction</field><statement name="STACK"><block type="controls_if" id="0wA:yL2:Gm`AffPm;uT="><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="-qK`4!,[=ZOc`F+8MxgY"><field name="WIDGET_ID">ButtonL2</field></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="=UOAMR%f.@);^;S5oL~K"><field name="WIDGET_ID">16</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="VR11L2nt^7X_Buevjfo@"><field name="NUM">100</field></block></value></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="4]9@pZR#|RvF^/x4z`xK"><field name="WIDGET_ID">ButtonL1</field></block></value><statement name="DO1"><block type="vexv5_motor_spin" id="FT4YMqjAuD`iPlLLZy#;"><field name="WIDGET_ID">16</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id=".}OuA^eF=`4)Dyq:vQQ:"><field name="NUM">100</field></block></value></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="#Z1t)sTzPbXNN6-#)MuK"><field name="WIDGET_ID">16</field><field name="p0">HOLD</field></block></statement></block></statement></block><block type="procedures_defnoreturn" id="gIkQVkB:Wp@?1j%:K}3%" x="598" y="654"><field name="NAME">flipper</field><statement name="STACK"><block type="controls_if" id=";VtR_rY[6]DBrocn8uBe"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="/:23YY+@m1_ImpZ4Paeu"><field name="WIDGET_ID">ButtonL2</field></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="wN9F,dSnx@0:jh*SWq7|"><field name="WIDGET_ID">17</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="yq(5S0[eZwEjbj3+Dza4"><field name="NUM">100</field></block></value></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="GqMxOjCila^11`geP7Me"><field name="WIDGET_ID">ButtonL1</field></block></value><statement name="DO1"><block type="vexv5_motor_spin" id="C7?#EV/?|,VsIo]h`[bV"><field name="WIDGET_ID">17</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="j@*+BJ]eO@bv,G[+f35D"><field name="NUM">100</field></block></value></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="^NDD*RaYjkj-rn}C|[pM"><field name="WIDGET_ID">17</field><field name="p0">HOLD</field></block></statement></block></statement></block></xml>
"""

import vex
import sys

#region config
brain         = vex.Brain()
flipper       = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO18_1, False)
flywheel      = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO18_1, False)
flywheel_2    = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, True)
rightFront    = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, True)
rightBack     = vex.Motor(vex.Ports.PORT12, vex.GearSetting.RATIO18_1, True)
leftFront     = vex.Motor(vex.Ports.PORT13, vex.GearSetting.RATIO18_1, False)
intake        = vex.Motor(vex.Ports.PORT14, vex.GearSetting.RATIO18_1, False)
leftBack      = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
DRC           = vex.Drivetrain(rightFront, null, 319.1764, 292.1, vex.DistanceUnits.MM)
DRC_Controler = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

direction = None
on = None

def flyWheelControl():
  global on
  if DRC_Controler.buttonX.pressing():
    on = on * -1
    sys.sleep(0.3)
  if on == -1:
    # ERROR: unknown widget #18
    leftFront.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
  else:
    # ERROR: unknown widget #18
    leftFront.stop(vex.BrakeType.COAST)

def driveControl():
  global direction
  if direction == -1:
    # ERROR: unknown widget #20
    # ERROR: unknown widget #19
    rightFront.spin(vex.DirectionType.FWD, (DRC_Controler.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    rightBack.spin(vex.DirectionType.FWD, (DRC_Controler.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
  else:
    rightBack.spin(vex.DirectionType.REV, (DRC_Controler.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    rightFront.spin(vex.DirectionType.REV, (DRC_Controler.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    # ERROR: unknown widget #19
    # ERROR: unknown widget #20

competition = vex.Competition()

def driver():
  while True:
    DriverSwitch()
    ballController()
    driveControl()
    flyWheelControl()
    flipper2()
competition.drivercontrol(driver)

def auto2():
  global on, direction
  on = 1
  direction = -1
  DRC.set_velocity(65, vex.VelocityUnits.PCT)
  # ERROR: unknown widget #16
  # ERROR: unknown widget #18
  leftFront.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
  DRC.drive_for(vex.DirectionType.FWD, 49, vex.DistanceUnits.IN)
  # ERROR: unknown widget #16
  DRC.drive_for(vex.DirectionType.REV, 35, vex.DistanceUnits.IN)
  DRC.turn_for(vex.TurnType.RIGHT, 100, vex.RotationUnits.DEG)
  DRC.drive_for(vex.DirectionType.FWD, 22, vex.DistanceUnits.IN)
  sys.sleep(1)
  # ERROR: unknown widget #16
  DRC.set_velocity(75, vex.VelocityUnits.PCT)
  DRC.drive_for(vex.DirectionType.FWD, 12, vex.DistanceUnits.IN)
  sys.sleep(0.5)
  DRC.set_velocity(100, vex.VelocityUnits.PCT)
  # ERROR: unknown widget #16
  DRC.drive_for(vex.DirectionType.FWD, 19, vex.DistanceUnits.IN)
competition.autonomous(auto2)

def DriverSwitch():
  global direction
  if DRC_Controler.buttonLeft.pressing():
    direction = direction * -1
    sys.sleep(0.25)

def ballController():
  if DRC_Controler.buttonR2.pressing():
    # ERROR: unknown widget #16
  elif DRC_Controler.buttonR1.pressing():
    # ERROR: unknown widget #16
  else:
    # ERROR: unknown widget #16

def flipper2():
  if DRC_Controler.buttonL2.pressing():
    # ERROR: unknown widget #17
  elif DRC_Controler.buttonL1.pressing():
    # ERROR: unknown widget #17
  else:
    # ERROR: unknown widget #17

