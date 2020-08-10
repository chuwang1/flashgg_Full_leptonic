// include path /cvmfs/cms.cern.ch/slc7_amd64_gcc700/cms/cmssw/CMSSW_10_5_0/src/
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "flashgg/DataFormats/interface/Photon.h"
#include "flashgg/DataFormats/interface/Electron.h"
#include "flashgg/DataFormats/interface/Muon.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"
#include "flashgg/DataFormats/interface/HHWWggFLTag.h"
#include "flashgg/DataFormats/interface/Met.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "flashgg/DataFormats/interface/Jet.h"
#include "DataFormats/Math/interface/deltaR.h"

using namespace flashgg; // makes flashgg sub members visible 
HHWWggFLTag::HHWWggFLTag() : DiPhotonTagBase::DiPhotonTagBase(), mva_(-2.), JetVector_ (), Cut_Variables_ ()
{

}

HHWWggFLTag::~HHWWggFLTag() {}
void HHWWggFLTag::GetElectrons(edm::Ptr<flashgg::Electron> Ele1,edm::Ptr<flashgg::Electron> Ele2)
{
Leading_Electron_ = Ele1->p4();
//auto leading_ele = Leading_Electron_4Vec;
//Leading_Electron_ = Leading_Electron_4Vec;
Subleading_Electron_ = Ele2->p4();
}
void HHWWggFLTag::GetElectron(edm::Ptr<flashgg::Electron> Ele)
{Leading_Electron_ = Ele->p4();
}

void HHWWggFLTag::GetMuons(edm::Ptr<flashgg::Muon> muon1,edm::Ptr<flashgg::Muon> muon2)
{
leading_muon_ = muon1->p4();
subleading_muon_ = muon2->p4();
}
void HHWWggFLTag::GetMuon(edm::Ptr<flashgg::Muon> muon)
{
leading_muon_ = muon->p4();
}

void HHWWggFLTag::GetLeptons(edm::Ptr<flashgg::Electron> Ele,edm::Ptr<flashgg::Muon> muon)
{
Leading_Electron_ = Ele->p4();
leading_muon_ = muon->p4();

}
void HHWWggFLTag::GetMET(edm::Ptr<flashgg::Met> MET)
{
MET_=MET->p4();
}

void HHWWggFLTag::GetPhotons(edm::Ptr<DiPhotonCandidate> dipho)
{
  // dipho->makePhotonsPersistent();
  // auto diphop4 = dipho_.p4();

  // Get photons 
  // flashgg::Photon leading_photon = dipho->getLeadingPhoton();
  // flashgg::Photon subleading_photon = dipho->getSubLeadingPhoton();

  // Save as dumper objects 
  Leading_Photon_ = dipho->leadingPhoton();
  Subleading_Photon_ = dipho->subLeadingPhoton();
  
  lp_Hgg_MVA_ = Leading_Photon_->phoIdMvaDWrtVtx( dipho->vtx() ); 
  slp_Hgg_MVA_ = Subleading_Photon_->phoIdMvaDWrtVtx( dipho->vtx() ); 
}

// 2 jets, electron 
HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Electron> electron, edm::Ptr<flashgg::Met> MET,
                      edm::Ptr<flashgg::Jet> jet1, edm::Ptr<flashgg::Jet> jet2, std::vector<flashgg::Jet> tagJets_, std::vector<double> Cut_Variables) : JetVector_(tagJets_), Cut_Variables_(Cut_Variables)
{
  // flashgg::DiPhotonCandidate dipho_ = diphoVector_[0];
  // // if (!dipho_zero_vtx){
  // //   cout << "Diphoton vertex is not zero. Need to recompute" << endl; 
  // // }

  // leading_dpho_ = dipho;

  // // Get photons 

  dipho_ = dipho;
  GetPhotons(dipho);
}

// 1 jet, electron
HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Electron> electron, edm::Ptr<flashgg::Met> MET,
                      edm::Ptr<flashgg::Jet> jet, std::vector<flashgg::Jet> tagJets_, std::vector<double> Cut_Variables) : JetVector_(tagJets_), Cut_Variables_(Cut_Variables)
{
  dipho_ = dipho;  
  GetPhotons(dipho);
}

// two jets, muon 
HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Muon> muon, edm::Ptr<flashgg::Met> MET,
                      edm::Ptr<flashgg::Jet> jet1, edm::Ptr<flashgg::Jet> jet2, std::vector<flashgg::Jet> tagJets_, std::vector<double> Cut_Variables) : JetVector_(tagJets_), Cut_Variables_(Cut_Variables)
{
  dipho_ = dipho;
  GetPhotons(dipho);
}

// 1 jet, muon 
HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Muon> muon, edm::Ptr<flashgg::Met> MET,
                      edm::Ptr<flashgg::Jet> jet, std::vector<flashgg::Jet> tagJets_, std::vector<double> Cut_Variables) : JetVector_(tagJets_), Cut_Variables_(Cut_Variables)
{
  dipho_ = dipho;
  GetPhotons(dipho);
}

// Untagged
HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, std::vector<flashgg::Jet> tagJets_, std::vector<double> Cut_Variables) : JetVector_(tagJets_), Cut_Variables_(Cut_Variables)
{
  dipho_ = dipho;
  GetPhotons(dipho);
}

//FullLep
HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Electron> electron1, edm::Ptr<flashgg::Electron> electron2, edm::Ptr<flashgg::Met> MET,std::vector<double> Cut_Variables):Cut_Variables_(Cut_Variables)
{
   dipho_ = dipho;
   GetPhotons(dipho);
   GetElectrons(electron1,electron2);
   GetMET(MET);
   //std::cout<<Cut_Variables[0]<<std::endl;
} 

HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Muon> muon1, edm::Ptr<flashgg::Muon> muon2, edm::Ptr<flashgg::Met> MET,std::vector<double> Cut_Variables):Cut_Variables_(Cut_Variables)
{
   dipho_ = dipho;
   GetPhotons(dipho);
   GetMuons(muon1,muon2);
   GetMET(MET);
}

HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Electron> electron, edm::Ptr<flashgg::Muon> muon, edm::Ptr<flashgg::Met> MET,std::vector<double> Cut_Variables):Cut_Variables_(Cut_Variables)
{
   dipho_ = dipho;
   GetPhotons(dipho);
   GetLeptons(electron,muon);
   GetMET(MET);
}



HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho,std::vector<double> Cut_Variables):Cut_Variables_(Cut_Variables)
{
  dipho_ = dipho;                                    
  GetPhotons(dipho);
  //std::cout<<"passPS"<<Cut_Variables[0]<<std::endl;
}
HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho,edm::Ptr<flashgg::Electron> electron,std::vector<double> Cut_Variables):Cut_Variables_(Cut_Variables)
{
dipho_ = dipho;
GetPhotons(dipho);
GetElectron(electron);
}

HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho,edm::Ptr<flashgg::Muon> muon,std::vector<double> Cut_Variables):Cut_Variables_(Cut_Variables)
{
dipho_ = dipho;
GetPhotons(dipho);
GetMuon(muon);
}

// HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Electron> electron, edm::Ptr<flashgg::Met> MET)
// {
//   dipho_ = dipho;
//   GetPhotons(dipho);
// }

// HHWWggFLTag::HHWWggFLTag(edm::Ptr<DiPhotonCandidate> dipho, edm::Ptr<flashgg::Muon> muon, edm::Ptr<flashgg::Met> MET)
// {
//   dipho_ = dipho;
//   GetPhotons(dipho);
// }

// You need this because HHWWggFLTag is derived from another class 
HHWWggFLTag *HHWWggFLTag::clone() const
{
    HHWWggFLTag *result = new HHWWggFLTag( *this );
    return result;
}


