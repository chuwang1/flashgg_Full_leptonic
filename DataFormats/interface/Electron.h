#ifndef FLASHgg_Electron_h
#define FLASHgg_Electron_h

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "flashgg/DataFormats/interface/DiPhotonCandidate.h"

namespace flashgg {

	class Electron : public pat::Electron {

		public:
			Electron();
			Electron(const pat::Electron& );
			~Electron();

			float nonTrigMVA() const {return nontrigmva_;}
			void setNonTrigMVA(float val) { nontrigmva_ = val; }

			float standardHggIso() const { return PfRhoAreaCorrectedIso_; }
			void setStandardHggIso( float val ) { PfRhoAreaCorrectedIso_ = val; }

			bool hasMatchedConversion() const { return hasMatchedConversion_; } 
			void setHasMatchedConversion(bool val) { hasMatchedConversion_ = val;}

		private:
			float nontrigmva_;
			float PfRhoAreaCorrectedIso_;
			bool hasMatchedConversion_;
	};
}	

#endif