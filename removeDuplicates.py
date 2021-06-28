# 1047 - Remove All Adjacent Duplicates In String
# You are given a string s consisting of lowercase English letters. 
# A duplicate removal consists of choosing two adjacent and equal 
# letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. 
# It can be proven that the answer is unique.

# Examples
# Input: s = "abbaca"
# Output: "ca"
# Input: s = "azxxzy"
# Output: "ay"
# Input: s = "aaaaaaaa"
# Output: ""

#---------------------------------------------------------------------------

# this traditional looping solution works fine for short strings. 
# It didn't pass leetcode's test cases that has very long strings, of course :)
# a better solution (stack) is coming later below

def removeDuplicates(s):
    
    def index_to_remove(s):
        if len(s)==1: return (-1)
        if len(s)==0: return (-1)
        if len(s)>1:
            for i in range(len(s)):
                if i == len(s)-1:
                    return(-1)
                elif s[i]==s[i+1]:
                    return(i)
                else:
                    next
    
    if len(s)==0: return (s)
    if len(s)==1: return (s)
    
    s2=s
    index=index_to_remove(s)
        
    while index!=-1:
        s2 = s2[:index] + s2[index+2:]
        index=index_to_remove(s2)
    return(s2)

#---------------------------------------------------------------------------
  
# another solution utilising stack data structure 
# to pass leet code long test cases :)

def removeDuplicates(s):
     
    # This list will act as a stack to hold the string that has no 
    # duplicate characters
    
    no_dupes = []
     
    # flag to mark the current index of character
    
    x = 0
     
    # stacking
    
    while x < len(s):
        
        
        #pick a character and add it to the stack, given that it 
        #doesn't match the last character added to the stack
        
        if len(no_dupes)== 0 or s[x] != no_dupes[-1]:
            no_dupes.append(s[x])
            x = x + 1
             
        #if the character does match the last character added to the
        #stack, then remove that character from the stack
        
        else:
            no_dupes.pop()
            x = x + 1
             
    # If after all the stacking we end up with a empty list, 
    # then we return an empty string
    
    if len(no_dupes)== 0:
        return("")
         
    # but if we have stacked characters, let's join them in a string
    # and return them as a final output
    
    else:
        new_s = ""
        new_s = new_s.join(no_dupes)

        return(new_s)

#---------------------------------------------------------------------------
# Test Examples
# s = "abbaca"
# s = "azxxzy"
# s = "aaaaaaaa"

# s = "niefxkwcunphbrmwifwatgwbkqxhmxkoskkkonxtssiwoebwbhfoqhervdnipfaahkcnkbdpsjeqatrgerptnrhhulixktlebkqsiqwtjwxquljlovbevclwckmfbsqpeqxulwddqnvchanrtbxmmmceeonqqjdfepvxpaglgdkluvhexqoaodllwkhmecpkfdvarcehgscoahoaowqlquiqmcgmqcrkkrtkmqrkdqjagjurlitjndnhkkouruuiallkenqksidmsbfldqbhbmpelpdrjfnsthbcnwojxoeoiborcmpiicclelboojxlpxbrewwffwqdnfdrupkqpkjabumxtthwajxrttnijutglshnunvubxapwfbjfiqrrapwjopxqnjurmwlxclicxempssqxehwhqnexwowethaqpwnbckghljsxpewvlpsgonalnjcjexwggqigcmudcchtqtkdifbsmtgaikentwdowkqbmhwkgenhsufwxfxgquqscfdcuisecqjiwohbmcbgijnrwkahvsvgbhcftkiuhnxvdutcpbqwfhfahaqjhcwhouvkvoqtrogfxxhlumerxlkhwelakirjippuusguehjtwcoqxasejpxtqkuasjsabugjoixutswnerflliwtqjrxjnrmeplboqmdofhvdoxfwixkobejwllhncubspdpsxxxiwqfpnkixcqirpxmjdjipmttcwdosebbavqqmdjcsnvstvngddqfehawhordkuxmsatqwvbovercopbesrtkqrqfvnjjfsvflculipwsmdrwwkorjpxtwlhvqffeatpangpmhemqrwacrkjlvdhnlebcmeuixkjrgcjxhqhvrbdibchmiqplkgsioehkvewmrbvbmidnjqeocosjarmrjfolbtmvhfumcwpnraetuakhclpgxmrecoiortxnjpfpvhuxslwuodwxdfchlulxjmowcslhgbhxhxqdvwemlgolbphhhvngdukxqtefdnmqckwwemupxvgoswcdxkenuscvxjpompsaedctlkarwujeingxarsjijadecxdmedbqqapilfvfitspbbpuvwvsvrxjrasaimqkufefepqptrlmngorkjnplcducpwtwbrglvawicwikgtlgqbjmjocxnmirpdlloarjkgiucdmjwgaaueshskiuxnbrvvskgifsldpdtdpnwbwohdxxxqvhtudqmjuphgqkrbpsjrvikhsetkvaubetxdtbrkgauwnnswdnislqueihfewoodsfoxdaxeewamaxkwahdcdplutlbhavaqdaltbrsmcirmfmddcmieldqmqtlmvbwpcjunaipnlijjajelurbgggjpctgcthfjflthubjlesnqwqojdcecqorjoqimfrrmvdooranlidrvrwxscclvvvnxaguniumtbehwdjopegbehptqpwddsjieeifkwuncddtthrafmqrqtqfbtrqxbfhevlrpuwvwpuwiqkirevfprdrbnqgpquneqssapukclkudrjjnxijlnfdcpwbvcewoakvikdhcbjbwqcxhknjqudjcwqvwlahikgwurarsfwanrjxsirqmixmevjnvhmlwcdjqavtpvvxogdvdgaebpokubwxatlxslusadismlbaducmnifxfuvwpwkobbtwkkovqhlrodpbbidimbuwctgniacnnhhebtuotguepkcmuflvuodwmaxctckjaqlwestaownavuwwipeabttbbxcrnrvovathvcxjfseatfruqsevadtulfnhbahrkllesptduglroamiksvhululhutatuvurnpappdmggaoqkgpqtfccxfrbcpwpbtexttpouvgahwdhpbvpcglmcaencxhcsmmxplonckggdivpcbfkrovibjxgqwxxmesxpdbphiauimhcitfowamsqvnjiprktrbrgxsqvlqwbfgwekqiehnukxmsxarhcmesqehviokpkhnwldjcxrtemegfhumdgmbojeebwgcexnjorcgamjtfkqafwhfrdccbwuuaqwujmvmdckrinkidxopahnjvenewrqdxftdcwcvabxpeisxlasfiocteowusqmwjxifcpivbdwmbqmsqbjpcxkpjfmujgnqctsupnlkdddmdjeqonxrrxrkqmjrhxfngnmgtthirwbtgxgccbxodqthnarxxhskcqtvknichinfngfpxrgukqelfvbbpsgcjjdgkpkebmsgvkpijixwlsajlwunjfwkplxffwrdehnjcixdmlpxkcdndipwcsxvqelgjurslnbuqdrdvnjfsmjekwwhvxtirwunixofcctskprnolkcrmwjtgmgahqwnvogoknbnbgwgqtmwjfdjxwjsbonngidbwmvbbakrgxvwcenglpexhfptghrbjjmxvlflimsrpjdxbwluelbwkqxdxlgqkoufoourdfqswbmusosdjoomlbwnriafpkaoesexxangpdmdxixhvmplwnhnxplwkldhlccrghxdachggqnnviqaprxaxxdfbmrkrldkoprulsbskcbivwnxtpbrcjuphrxfiajhcnaomqodhtwmitbmeusmhmkpqnqenormwthlracmcfifudkcivevisqtbgjrlaxvxwlsunalffuicrcwkugrkxufmpvcplggplpmrewkgifqjkomohbtaqicxmqsnkmcmehogaogpairljtqiilxhijgvjhwqkmwqxqnmgfsgdiamtdfmvaktemucsvqnhjwrpnukbpugdjacttjpidwialcklpwiujgchtaswaomvqfhwxwdhqbbpdkjqamevwbanvubimncgidaxsrofmhcvqjefemwpwmvdhetuxnvrghilcflnckjhwcvoaecgddhhwudnnbkrnuufcigvhiqbidshxpdfkciuniwichumrwpcnmlqgfdomowuoswrxnowrvpajrxupcpwboxktlitminrqxpnwpminolcauhhtcgmqsmptijdofdskmbwdvgiwqgcrejipnqihdicrpkdmrneourhrdrbgnetkuhtjelhtogjrerguhnbtmtvgfxxudqbnrhlnfjfopchauibqejwkxclmoggbohrxxlwglwvfsqacktpnumhrrdojmqcuimxusjpishldlvajsqvhlsruwsbxrdpwhewiwmsiwauontlmirxkehoglkjdckbfgddpwbtbmfmrgafujsibnamtdqkkkkeejurmqcwhpbwqixcxqiucipnqsxxwxfmiffnvovpxlrxopegjrxiicsxamvuetjfenhkvuecnvjsrbdnmbtqogduiwdgxtqlvnrfxanltauediidxthxkkqcllabvsicnsnjbutoiipijspfllijwqvlnqoibwupdoxlfvlxvcvdhafnonklpfuvdxcqpjqerafgqhpcaitrrbnqewajjnskighusibotbjhwwmluifntilkqrxorteqiqlihxbbvoqslvpwwogljadawscxamnkachkdcwcuuvclrtpbeeahojudowxnviduwstqedlepvlswudsaaqbojlkxptlxubhkocddmshjtkeioeunbokdqcxergwjcpnsiqabvjdqvtmlfxtabgitbthwxvrgpjkqludckfupvjakobuefvvqaufdvdkradlseqaeadvkpjccdesvqpohbxgwjntphbedpqtrbfswjgqhsvkpxxxlqcvtnpsukoaahbholraonfmvorxggkncjpxwoujteadtbhspjskgpblptkvpalkwbegepifrrsbsjngihtnkmxjcvwbvkxcmcmrificdwaqrshbmrkmpqkssjxxfqrtiskjpuqulnorcbsvbtrdapxstrlrrvwqomeflhdxverctcspjsgxbmrvjluvhgkvbmvoclggpvdohasdabmmpmfohkapdhpvggqkpmexdwbctaxneehemkwtkkscptugjplehfrnwshbbgerpxcfpurwghnkbhtkwjbbmdtteorxpfotwoldrtcfhnpumxawrsguvkloqutjakaxvvnjioecbjdtmoiovnwsdvqtqcskbrxaqiethplkpnmtwrxpxwfodjeuwcihvvoudeuvctncoxajfmatlbxessdohcktqtcnjmrvfnducckinkawvdxrmlcfpnflgxgjxmxunslvgsgvtasgawlqtjefrxlseehkjqcifwjaatqlsjkgrqxgfqgcsvjufpqfkegesnqdcsehwcokmufgvdmppjeontgwqnxngkfrjbomdphnvgkupprsjbodafvbfnrohblfjokwgueeascniabwpanhdjiswsqmaipffuukkugmimrucbbodclpjlmfxpiborutcxadteepkqdgupfpdlghhwmvlageebpfflcffpassleghnaobxibppuapruhgtmnhngfndgjeabirixfjcxehrjqawpwamvaxxihgrtallmjnevbjrgrsjptpulvxircqxuguqktuasmpfogthiwnlrllfvbgccpvqhousqoudiwtgaauidpktufgxxwjpeltwllbejmmaikwemcqacwpudnofoomluboffkpbqddupftkjsdtbsikdhndhpuroxrbrxkwsfdckjpvrtafumpdixpoevmwnprgeuhhsabgtferaqnloccjnjsadtanwhtriabheobuikiblgeafaerorqhgvnmujavsumdgmhalxhlnkrpmakwidgvtaovmcpoxwnpjohgcnditwcwxbovwciimhhmbptijcxpuielpskhrpbisegsneklhhmgishhgtwoagtjirxkkrlsjxgqbtpdxtspuiqpqfgiuuiwapwgcimoiwiefmfkpqutsfkvnvmtrgwnsheghaqclmkcgegvvagvnmamiwtroalseouhkflrwvhnhvwbusnsstqpuuhwfvrbrhkfbsipnoukeetjqxufevuuhenqcdnxnoslafuqvslvtnpjmnpeinrpdbiqcudwlqjwsqliqncbnlivoacasjccwqufjfombikkejatleudjmabjdsanlfsdunjcsemksscbsrwcswhiddcjkcovauuwjajrpxkcldtoiimkmdarlhlckwpimedcmqbdquknhtrwxcavnxdwsghaodwhdrlfrbeurwbhrfhoddaicwddcfmxctiibpqccxhxwtrufwkcaoaavfonaqntdvjxsbonfhwjtniqxqvvcqshfpfxaspaecvhsmkcwuenlbbpurotnvdcmihwormkkapvmmgnisoqmlqfqvpbebaowmogwxsnirumwvqkhwhvawbwowmlvimnxapcertfluhjtdlvadmbnaigckkeknlnuxwgmtvgosnpgrtcwnbpnlrcqenaqorjrowacitfnrsduuefobsmvebenbjumfsmaxmjbgjuvurrjicstjsljgtjntbuawdmhilhhpeibxhebaknrtwbfxdvlqclrxgtcuqwwqgfvpaqqswtvlbknjvvlmhglkbhmqpjumfiophcsamgcdarfrvtsbnakmptjgdnljeliljntpxtvjpsqlxudfaobbulgucfibhtfqsxpltgribcmlinkdetovusgofoxbsnmivjcxvucfevletqepeuedmogotlmnbtgrpjpbphfdbgtdeduwfvwjwkjcortajlbhetutxuvwxkgehihlkbkjiktfdexpehqupslkiapcqmjtqficqmsxnkjefpopivaoftjcfvgdqratdueqtdljjgorjwljqpeqrbsofjwwfexsvlnagrbrqkhktgrmqdrhrrsdrwuobkscaeswgtaeocptwlfdeekvgonnwctqrwnpsvnwxvegxkdwhamrqnuaxvpqrpioafmpwjcfnsrliwfbcbqljmjmgbmiedgwtktviufolplgesehkeonkmatixqivqjmgsfeejlfnhnvpcrfmkckorklbtwvxewcebijxwhobpnkfccfejqatwvpeiedwkigcjgxdggobcnsswtnvfejnrvlgkmgpnutdjumgvtirntaddhaebrkovnmkwubetvnndgkdplihtbkstslmkvwdgrnnaosdhijkuiwwhblfjukvdrrdmlljioctdhlxfakgpomttrmxcivhaxglrodlhpapddimjbmwqmaxoapctjoeeqwqittnxishfopowimwmwneericptdaerwhlxpdmguufetrsankpibajruddsoxngreguljcucfgqpbqndvmvowjtgalsegbjldwpsuvpbmnqileusmqdicrlcoswjxoiaphurgjcewnhrskjhdomfidwnrmmbawhnvmhunkkpotaqjggnvtghmehsuwghexjvajdxeucobcrhhmbaxsttsadnuusahdcngtofplgotputnqoemaqfxdfsujsavapxqodmcutcxwgqqwqwrrrborjossttladjffvojbuxsklsnldrsassdxuuxsjfmrtgxnsajhnhqhpmgjmbsbhgsxjakwqjdosddjevmdtimcgebnodxbuxhovhvjmeodecmoataxcntpeubtwkceuswjlufijkqdwrhhcuiamlbbnichpksvnkekadvospnudeirwfilqvreewaonpjabvmxpqsivwkravtpqcfsppifpiacfwusofssuqijuebwqctgugjlhnkqilmqssopgpsjewdwvnqphoukwhciudsintkfjpecowqwkoolsncasoeochkhqgfkqeflnksqkaixsnosiidfeufgltxskbgrwbrikolegxhobngclbpjcwepxoepdrtslqcgfxmtwaxbsmtfpnkkpiefigobrrwittndrbrighotcwbiqqjmhmcltnplqvdiswebtbfqkqhpuntgkwgrpasfmqmdkjxvehfwokfgngodvpolrcpwsxxaptcewjgmmqtnhafhngxkaigebkhpvogaibmjncejqxcjaaixmmxprcgnfqsalhcilqoifhmxsvoaqnljamiindljtiunjarvekuukvtcqjlnadsjdsqqxwbnnakksefchusbpoexeoolhwamcjkdlxdmqsgmcqkmibnlaiukdhcawlsgjgkfwtwtaeongpoochaosphwcbsplfukunmcmvgwbqvcrntnkawoinjptiumbqjvhsfoirwhxcxapovnvrnxgafklpddvqgkwihvwdlnoiabnpranwqvblhdvemhccwvneilcirccmucwtdfhleuuknfpjrgvbpehsdebdlkhdqqhghgxtliekbvedatrjcikouepiwsqbhvlmqxbltvewiwpodckxoqiepxpengtcupxktvjpwhbkfnwnixngvfxhibnsgbkrvigtlmllcswdfvtgconkeojulgngkpldnguenpltkkxdulmtvlwagflxfleeqwaubeohfleksmrrnldjolnsrwrmjkgrchoatnpcxtefhchofqndxaooowxwlaoivqjlrpuqwevaljvxqwohohdquajcpsiffnviffqgpbuwuoijrscxwetcvbcmjkjfvrwevcxwfxovfduanqnqtthkgniinnudjjqdemgwvrvhkntwqtswbjftkhgsaqnlpbwrpgicdmgjprujfpxmmirsouxvfvjjrdwjqukecdfparimrroabvnsoxjwhslcmwdavbxcatgejdfdqvnmcnqpvmgbfrabdeisatlhwxughrxlvwwvvstnijlkaalsljsthfdqtunpfrihnrgwvjeqlxefvrbrqsfxndsxbotmpfpdujkngxhnkfffqsntodgjgbfceqeiblvlvdueeoopiuspgvllihxgwtxnkgcjxwiuncriueadrdxpkqqwksnscvukfntjvjubxlnnimotddqiagxwsjlbflrpbjrniktgqrtworgfqtqamkebcaxgkrjxmvbbleuqmrbrbbufuvvjksecwsehxejxioxajsqrhhkqnolnvvbihrtgmufwhgubrpxqasfqmgrqwoxdfikbftlagbipxuwdfvfluxhgqkmnqmfcackxkmsmioxajcuiwtuwhvjboavcqtqpdgwajxugqwpdlmsfagsvoihmdubeibeukqsoocukawnwxhsvarjtweottjepwbohrfsofionmrlsdnsmkbhnsnjcsdcxvhkddbcdsvhdkmwoslwwcbohwpuglipajpknfhwtcvsguccfqwridgtvogmkljxnovmidecqauumoacksahvkmllwwmlvmotjvuiqlbxioqqfkekspfjdoimklrdovpgelvrbjbenhcwvtlbwfwqrqhvpbgqchasnddabrucguplsxctjqhhbxmciuifuxmlpjtqfixxuhkjpdpdhctbwpspjishjrguojqnrrpnmvqhbdmgmjgtflhiobijfhlsopptjjojlkuwekwamxvpsagidexplqxjmxlhatbgmkkulfrfdctdjrkeutcfqgwncniudeeklchmdxrigfmsvkaqwdviavmbovlwvalpmmxshncxqdfjdrvatbfdgcncklxclkbstvesmsamvskkwxtpjpgkhbvmumqljgmxukubodherfodldpkdksjhfilqklntjxbeftcrllcaqvqopnfnpqnbcsdqcummxnwgeuciphugwtdsxjmuqrjknwhbaofatmqnrldhsjmifnkuapccltbosceabvtncguxrnderthaihqintvnsssqmigapfknpqgibnobqkbmdukjdqxxtqpnqnrnqmpfxorcuhodsdwpkasfgufwauujjvqlglnanessvijvdqjfbxofrbdvhxvxueqwhaalogwfcdcuagplmwsiifmikxpueoncnwesniognvvmfbmlhriaikvmxaftghlugkwaxgrbejpinmmlodgbfncdjutkndgpexbkhdjckmlnmvkgnqhrschdesgsgobovrrusfendrnhahlxanikmfqhldjkfdjpmftjdoehcesbcntvdntagsqtefamfqcgugkwpuvcvcmabvordmoqvfmdkepfchqntbcgkbnuxgbigriakxmoukidrdtqrgwbujhppsgqmnnuihmxvrcoqeqavoxtgpsxktolddncaksbqbhaixtdejhekkxhepgktbkojagwpjwlnmnjietsfllvucilpkxwkkhofnfavxmvbmkfpnwpwawwhsmrnmihdaruugnvgxjeankrsnrnecmlhpsopjhrchfpsodignhuxkqpoixbtwdjqulftuwqldojctlmbgeibbjmvtmgoafcogftvtkrkbjxjijxdwuflfbnvrekbeiefideibxxteqfkajfqirhbrlvqwmgbogbjxjtbjigcrjwsaoamabbotvqephrcklpwgtvujkcllxpunfntlxihfjslicvxlfbabwwttbhkxplvjsbcuahhmuxtlxxehgluvfrfmjjdilprbjhlxglkusehpmshitkmnuteqofcsbhdjndtrhqgkwdcneebuiivvqamdlvdcfhhfujgfxkuxgsclewbnrttkmtcjohlljkkqqfbiaetkeucfgxqarwlamjkwbgmstmiaflgfqtuwfnffqrfcnnpsnopwaglswtuajqliccgxmjbcorrfbefmrfnujmmxpjsdwpkglodapubfcstgbxhkodswocugblxwktqcflhpalbucjfqrctrauxgegfsqupohssjovhwmjftjslrmktfjtkkpcmqijnnbasobhwtpjjuuakmhknqpnhmtmotnwoawhoodvrqurjovqvmowtjvgbrepfhegflamjuxnmsbvjkswrpvcdbirvffaxrqwpkmewejjsfipfohnchhcpoclomtbouwcpjgcddvgxnwujwgclrjcnurpbssqqnavcmckteqhioprjvvbrkhpaortcdnpxpumdgdablvbrdgbbphfhefmeaealkkergwtxfoidnqavcaavqjdbmhmuoiftftsbpavclpxugnxjorkbgfxfoifofqmeovnkwixxwspqartakvdrsbuufnlnrjccdlksnrnciswsspaxlapckixfpsqvnfkcwdlecqsqonpqnlbbwvdgbpmjhdbcvccamhgmbhlfungvhctdvbccurghattqwllpkunfvemewhhvtpcqniacoscjaqjdlfuecwwnskasaogeowrncorlugutrmppalhsjjfpfgesgqqwlefwigjhakhkaujakjrvkqexjltatpaxptrwtgmejrabbdlsutfltiajcvdkvijlnblrwapeqhcfjhrrdoanhvwbnifrpxjgjkfexbeeuqscjkircfgcjdqdwbimepeuiittimbrobudibtwouclxvutxdgejoucnjkbhxjvenefjhgekhbplrnvhkeikwwsvaocguqwrjntiknpcdpatbqfpkvsuupbdbldcasxchebieumttqsrkhhfaxwbuklmjmqqhutkvuehchvqehccxxxehlbwrtnctgukmaawwkixqdhviatsgfcbliowioretumnfubrxkagccwhfrsvrukxbicpfhetgllvuljpsibgdchcwmlpvamlmireukdnxxofwrwffxweiwujqnbdonmaqtgqruagsuqdwctommuefctawjipxxhcbggbhairtngkkdehrsxkgsoluuwngdpoenurtjqshxtvmovdcojkhtspwcudfdrxmlegjfcwbvebrrbgcejalauqioitbfssfguknieqfmflvpgngxjppuxihvoknemsmxvksuieqajvluxdquvnpvogwljvhunuunnkwwuhummejmavgxsupohlktgwjjxsrkioltlnxntmrdngmdekkdevwkacqaitxcssowqifpkrigkcunwrnrlaoemfidcidtvbslbwigmxrploejfwukphomosvilxqpqbnwbdwnocsmeoxkuvdmlwsxixscvuskvvbllkdqdfvqkeknhcgsvjhirxuvgswsiqdxnprfxoxxpgpwubqaqfqmtfpvjnxboxxmkpwoaxmvqqeieggcqgcpcpxwjkrdthiaofvxhgqhjvmqovmmjxhvtxxnmmqfskdwfgsgdvgpobmclbotpefjccvmfxbtpnvsdvcfwjtdurpbkaarwsqisudrqapbpmhieoaauwdovabkumfmrekfqbnpisokwtieegimkqkuosgqischowbnhnbsdcctxotdxqovdttjmmdjixtoqviulejxudiipqtajrxhutmjjklpqvtvuvdfkclihcterpvggmonbuhblokgnjireqxvvcbsqcimkffdkvxuvjjlegettxuefehilshsthbtfiwljjxiuqnvkoosvluudfxcnutlmwuwhcfaxtbudlrsprdxhbmmswmokopjhkujlixpiajvoppgrtqvguxagdraesiqipgiohvnitdoqregsjhjwksmlrcohvkfdcmgtjonequfolmmigwwsfrnoltsidbkfxeixdntgexltkcgwharxlavbgbicaivabsroavltkqhlclwpxcgawlkrmgociebjuqwdglrqhmlmhukrkgbklvxtejgepjkmeulsidjhwgepmwfpncniguabitedrlengreibiiflcvdxquvlkwhdsjjecgucwtrgemrxirhdudctfjgjqckwdwnmbgkvfukxixqmvpxsjsadqbqcstotfdkneirafbnnrlsgmqtsmosnwrwcdohwsvvlarwvsahmlskxbafjbsdlleugqoatppjbafnbiecrcjnupjltutascwgrdqnfqnblaqjacjuallwjliitsuvwrdaqsidsjtdfenhwolhubfscbchvocftkxwgbjwmnnjujbshgorrblelfkgwvbmnspepcarispbesixxwhmewqbhdmpbjmiqefoatbakcgoatvcsurgalbuuouisiisagxiuppiprftujnwusirrxcsvdwmgvbiqsqwatpnrfxwmpdhqvqludgwvwxxbncowvmmxjfkuiccwbmcujvhuvkvjdjfnlixmtpxwheugqslllukkstboisdogkjjtpqqaorxirwswrvrkpuiepevbblgkfrwbkuuhthbrifmrumtjaeasdwfsmromoaccgqvvufffeuhuidouufpjfstjolkqjsrqxxxweicqcqbkaivhgebvaedjnkwkkdvkqoooxsrwffmaqouhdukjiiphcegfoxejgbgqbiqmdgfsejixpsgdbbfounnwakctvdtshpsvnxitqnfenbqnavjsfqbrlqclqibolbmnkvjbahfisnouppghccmkffivunlqtmjiemmobjorcetumdispgensvjgughojkotahvxwqmlbasqsnmwprtfmvriowpttrojksaalqcisfjwvbnphwgpixscdjrkftnpncjmuvuwjakartqbksbxtisfkuhqjgapwttavdhqmmcdcaibnjibqefhvlgamfshiamjsxgcnwnsnsjseopqlhfdbrsidlisawwqqtgbirhlvoaqlnksiobvsdxkbgfnkagejecqlseqnaiiflnbtdkjlujdjrfkjdradxwtavqotugfheubadweqjmhsxfpdkjhbopgdvxjdhflmlciudjjhntsvgqajslwpwagshemxlbgbufasnwfsvehxrcxcodqrmngxwvumnptcehpnpjkwvbenmacalvlmclkogmghkcfcxnodthwoailrdwuhvmjcwohnvxetepiwauuqxtfxstarkpcnwoxrkrafeqkuarjcmwmwfjrvixrifhgmngjmuabvbewodmlbwabsdoqunqasqloreplphpoxaxcfhfcidoijegvhwctmpgwxpoiwgleifftfshclgmfgddmchjdaomiduawwhawmksvdghivmnmngtcdtrhurckjexhrvjawwslbjaplqhicqskmxgssetxmfaavtsptditnwolbxmojutijoehalemjtxefxqwofkxkqgjcvscxakbavwdjsitmjarfeorerkumvlmdfdiwxmxtxcscntsampbrwimbkwfiisiidfdmneiwbcxvbcmcxpjvjturoiiqeobemsbeopahodiaqrwfhguorcuhgvxsxueemxecoqbadrpnpstxphiobkqaqcprehuegircrlrndibckdpkevplponxajmrhtfhojtqsftelmskwigcjvoqwsgjbhcguvlscnqjxjepgjfjnevedurbkdhkqxumpqtalksammhsbtxufthugeekxvegqxppeqapatoadbacagvvqkiwnckqrkkigshehchactqhjudtonismeefusqfnammftiwucssaqdjccebxohwlwiwqaspvlgikqwrxsxptmfqkwixqdmndshefhujgwmgqlmjuijukeqjffcsnsflghwngvbpenlkmbhshqvfhmrbxcxgjvuukppsqnpvtnosrpdienvnwqdtvrbwbbvnroakokaiibriupeqpdaameetbhwpasgqrqupfkrcvwjjjgvuuppumuonihsulujlfsagapvjhxbalatkxmptduwfhohsnltjiqwkugsilivkgbknnhvcvqqxahtfttqgimuiedsttwkchmwjilmevlaqqgbrqpmoafgunscwemcgcxldvubwqljsmiwbrvsfueocspondwdqkmmnqhxmbkatorubbiaiqxsfiwbusrjedbwvohcsmvjwelbxftakqknjsdqaprgqdifvbrwlwbaaieivrlgwhimunjqeebaglovlpqpdtaqtqqwaxmqslfbafokupvckkajckakqohxmgcwlwdikxncrnenudbbrjqgxiwsmespiaomtastaxnlfjrealshhptqmtvmtjmfcjruusvfjxrogopcufecqffdgbctlhluwmolbhskklmrjitmfuswhcbtkuikgvckihbextmogakhrsjwvlivjqvllkuiinubmvpdkdxeriavlrftsadvjteifgrgpdhohsueftwbxqjncalbxgwjvqbgmdtsfmnutrtmnwhjmubvemhcqjfgwtsbexgpoudjgaqowbmpeanqlqvtsvvgdpbmsficiogplsxwdxkrmratlrixpnrhgqdfrqkvmoitotfrbvorpjxjkcounxwmuduwmosorrwblhokepkuqffgribepopsieqmrsdajdefocmnxhdgvrpwxwxejwamxwlctacijpvkeqwppmmcccqggbkixloovgrgpekrvsxwinvcqidfbkujtfhmnrveoxgspkahahflvvhunhldphqtcvklxexlfgndrgxwpdcvruabtgiartxawvhkkrcwggemxutlfbekhwsdojnacmnvmkknbkcjpufdxirbawnuuxeqrliwoexvpipqxucbcdwsewmmrfcacupdrqlirrjvukbwtlgimqjwlkaihlxsxxjrjwtxhvfpxfovoddeqotdwqkkutaggvomgoecvgkbeebhvbublkafkugvvsbqtsrcmosmvhbogdnbnhojbiexusgfvmwdcloohkjqndidcipoqsecvldphpjpbmdmpkbfkvftiikctetumhsxexrhpnagnwmxweqkkukbkjujgognuqffcjsdqrjgnhuhuwercluwhsrmxxswekihsfkjopqludjklktopuofmognroutacxbjomtoepkovvcjgqgvwgdltgsjvxpfkxpcjgokcngrsfmjuquidgecufodqbifqmfdjkgigltpvotacoelptmufigtmnagojagsnpdnhwntsnqsgtkxshncluenwudssepktmxjvkoxomwkfttxfibxiosgchqxlttkqlaqitxggfpehticremivilddpbqbdobiolmuvetfeggwegukxdjgmrbwgttixebpjcdnnadbfhdjlaklvigoaamiballliorsdhqwqbvloxbftqcrjlbpohdewtgdhnsdjgreakedhneodjsbretwvxmcibgefbvkaldutbubpdvatkwxuospjhhrcqgrvxqbmrkjwtxbambjiomiodhaquxlausxudfmrwtpnmchaudugswpmqquubcfwrpbvqcjmvbstpkwcxqfqrskirqirtdljcacfcrkpsqhvqrtcqtbdqcdatehunvatnsbioxeiqnbonukuvildkdhpipfbmgrkfixrqitkvuuepoxmrmptmbrrnfwulqsbwwsodiljepmrmnvhakjijahkpdxipixmurnqmdpjrewjamrqopgnwddwavtselmhdfugwmehipfrwppcpgjaxiksnvowmlephuekwrgvflwndrllqtwtpkaqtkehgnmgmuirpvrjeulrkhjwldkscejwmvckueqsxjegoliwbhkqiouifbikvuqxwmdcdwmgcofowbriaxoxiartkcepmesxmkeewgmocxgvubwdfjebpcufwbknkbdtbuhurhlgljdodauuuigdjqbrnsxhmxxvtncwcxwdkpiwakgfjitrrwtdecosvtsdusivcajxrocrxdkmrompdaphfmtjswhhkogoxqxafbdkdxcmwnoamsbbvvlrwxlpinwunjoakmcgqklrvbgbaxvvjarwwrcwcuomxqqffmqjdirpkpxfcvhqtsrmvaqadwkscrctqelwaehkclorghsubvpoqxikraurcqaujbwssetwxqorjalhnaibsmpgxfcgkjfvkfvbgkxiwkdaxvwmnuhqabjkbbpfwaplbhvgpeiluwbllkxpdxqqoekrtbqrdqiribjojejllhuocmsvnnxvphoxrippupvdvxvusximrrjmpncivrjkphqixdcloxjfknnodjxcabtcxjuwbhjetqnarvnbfoslvrwvdgtjwshmfwucummhpojmdkcuuocjrudqukqovjivgxvqjtexgfiobhxaamoujmqrcrrutrckvifmwrpxeqvexixteuswtesfkwegcorhpuwcgjqtxforbxxxeskncjmipptkanbhirnwehubixvbdcriokjuswcvwgluirhhlbwfgqotwjgqbfddlqmpphqrtjawnhwdmjecpxkfkqplilqesqhlmbdhrsvvnkdwqvfjlqmfdjsmcifpmngchxoemopgthavdsdggqbnkonrmbfpqnmkdwvujkkmtrlmajlfullrgmkvdbejasogmbmteqcdiexodrqsjtrojxferegjqcacofiuqfthinjisfikjxeqptmkdxqsnhgsvemdkuauwxmnwjnhaaktfertgnfrkwukvvfonlpxogelnaupsmocovjmudjrmtfgsjvhwvbcmhnudqjvlpusheaaluqixsxdihklavnlenmuulxvxljhmdcsvvxxwhdeuiivqjwncvuicxeucxhuaisqijjvnoaeisbsbdpuscrmeosuqufginfnguducsrrratwaafeijpuunotoaeaxhxgftprorjhlprmanerifttgalmghsqrtmvxrdhxnfickxbweqipcagxdhcvmcxutiistkmjujrtokjwsutpvsaksmuidqmbmosbebrharxagfxdlvivbogmbxlbjrbxbdoiikfwwifgoeqrthcntxurlemnjhdpidckmtsjsdhkldaffovlwbfuwpebpqfqmksftqfvqobgixctpooewagbelvxaimmrdaeslbfevpakddwtkxkijtwdvvfhjuhcdsleclgkuokuthdppgkxpqmnjxfjbbomwcwfihegoackmrfvbgrqwijplpfjmwmuqwjscicualkrrwrkusbwlxbnwcpuuqgunrxwclepwkiugbslliqfrtxlqcrehsajqhogwmhfujwipanslmqsmoavlvnaqjnxgnjnsohinesarfvuaqpaiephlobjdjjctvepigxvwahaxmpfwchustbfobiovnrglfujoitjlhqvvcoqrmobvvcdwsfqbkbhrhdoxhbwixdsqdxlumgefwnmbngndmmqsrglqisjrdlmldfjmnvxxewgbggiioxhkgrtthunbpeoknfvfdobwbclskbgcffondatoptanxkerwtvdlftgreicutkpnltxkxvuvcnrpalvrklkhndtccbtipjtruatrlqcfgibeugbtwufvencofcksdoawvkgcovdktuqqrsrammbqnewrlhtwknuabvutvdtjdhujtkcuixsummliiekqalckvfjpvlwovlpkgthcfjdnfknhxncnrtxrnobcqtbudvnpghuoioshdjjcfobxjkojmmhrtwhijjeuxvfoecrwmvcencremtdnwcqodrmfutwwvopuoafxtlncuxwhocckiwahcpmqahjhubfvbosnmxexvpoeuexdwdtpgvmfqrhnbpdmsgldttvrnidaiepodumkboxiqnelowfgugfaeolrpucfpxvudoiujwkevhwvqbqpeavfljdgqaprnagudglrjcxgdsxxdnhkfbehvsisdaoxgtuapgjnmfmrfeevtnoeunbtefwcviccpnnnctffidusaxjuvwkrvqxdnmbrsujrsjfxjbnuxbmfhrkhtloutgrfuvfmvifvmuwrhmtwhdwwhucbsiockdumfuphkxldsrwpjpuxleqidvoixsxxhdtmfmkowhwaonixcqdlhioqqqkimedowkurgbtmfsuowsrdxcwoxdsrrjslxdqmsdbafivgcwhtextalihnockalusgcssfquathmmpsfecvnmjlqtckjbbsmnwtvdutxciokumaewxglxtduglgtexbxqgmjboabwchfbrahtpckjkorllgefxmaxsdbppkwpfpkqbacnmuavsalagwrsfacwoskcsosafqdurbrrukqhgoohrsfxejcioxpmexrghqxcfkitkoxdsugnogewbcvsgnedikpvvjxnqvtxswioenpotwdfahfidxgldsiifrbjponiqfitoovndovpevhoxtiwbmivstrcwkmtaxkoukdpcshjkqpqaupcwlcgqckmiesegpslufpqexufwdjjrookvemitmamcbvpxlvhaflmnhqbldjggerldlqgpuivivhiwggfudnhjhiawdktmmnhdduojfnevlnkpubbowxentihdikunjnmcqccevdlohdcwrlqaagaeqcjvvuuhpgnuhphtxxigovmpbivwnohbqmcrxdjfslhnehrmhewdexuwatmokdnkisgksensgbnikwucjpkxmfnqcqkckjotvhkojmvvhslsgqlcrtpwlluhttrokuvwjxrhivmhrnfodilwtnjfemfrhbpxoaxisppbmmafadirouaesimqmwubsoajrqqwkcabandeadxxkhwgeindodftinoaxcldwertbecpvgwleujkvkxrxrdmvkxhfigttcnttuiresscpbudpjgpkclonjwlpatkearujdtapcniqauvhbwqmdbxvxiiqupeurptaenqdtnilwfnrxubjirkhahbfboobjvldktdeioxkpsvbplgefgcqhjtrtlsveobxljohgsjmxjtlehdjgvguirbigmwwpxrxjdwgqhjdcecdsvlnhspiieiiolvxgcpijugokiudmaogfaddlrsoknmcxnledowvpssurcobjblokmwrawmecqrvunmanusthxgkaikjmsfanvbaiuhmvrktdbubfrbvvhggeovwdjbqbiigjqblgnlqwtacrcfavqpsiitnqibdcqwxfgfoshsjtidxvclhdutualhrrmddejigrchhmtrjmejmlogpsaqwjbwhiqcwuicabpumrgnvgcgvsrduiaboorusckkogaxajdoiesjjfiwglogrhisguemptmhrnnmtfalwrwsavqfdmmcsvthuoqtrxlojntfujdwmftmwcphajueemxvtqquvctbudpfabxdvthcjaijbnuilrwggpqnoqqgmcubcqcompejslbgkexbcaeqloepbuvapwgnxugdhobfxpecxdsuwvpwfsjjjehtqmsmdxawrdhjmxgjunpvkmbuqosftksdcxldjheewtmkmjdpwgehlbxgxwmidesmtmngngvarblumhpaptmpuqvqqpcfeusdoguaurbwasacpgnbepmbsexpouxckpicgrvwcuckorabskcfbxhaadjffckqdcwpjctmclmihsgfaxcqlojbthgijeegixafsfcfasnuxsgrgjrwubwxwwttgxdoxteivugwsvadcmesaukljtdqokmsqwsvmbeeogmtriqhenfebeltpitfhqmjtnwgkpgorepplwsoraecffgdansvmejftjjggquqkemhmfstfrvbbcqnkfmkbcnqevbbdhcqfrnohxlcuvvnrrehhewbdonqkfrkgcwbgaajrjtidphbimqmnxdwwefikoogktkhruquoiehuexccjwqwcqufqqegtljextwsckdqgtfexjlestxqpxaffliljegadflnnjjgqtmxesrcedgwuwnbrdqvtfkrrmqwrblkskkcqfqxljhdnaifwrbjwdjtgdlbdouaascxgweqlliffsnxjmorviwtg"

removeDuplicates(s)
